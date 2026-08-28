from fastapi import FastAPI, HTTPException, status, Depends, Security
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime, timedelta
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from jose import JWTError, jwt
from passlib.context import CryptContext
import logging
import json
import sys
from pythonjsonlogger import jsonlogger
import os
from functools import wraps

config = {
    "SECRET_KEY": os.getenv("SECRET_KEY", "your-secret-key-change-in-production"),
    "ALGORITHM": "HS256",
    "ACCESS_TOKEN_EXPIRE_MINUTES": 30,
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()
limiter = Limiter(key_func=get_remote_address)

logger = logging.getLogger(__name__)
logHandler = logging.StreamHandler(sys.stdout)
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

app = FastAPI(title="Task Management API", version="2.0.0")
app.state.limiter = limiter

class Task(BaseModel):
    id: int
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    completed: bool = False
    created_at: datetime
    updated_at: datetime
    user_id: int

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    completed: Optional[bool] = None

class User(BaseModel):
    id: int
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., regex=r"^[\w\.-]+@[\w\.-]+\.\w+$")

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6, max_length=100)
    email: str = Field(..., regex=r"^[\w\.-]+@[\w\.-]+\.\w+$")

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int

class TokenData(BaseModel):
    user_id: int
    username: str

tasks_db: dict[int, Task] = {}
task_id_counter = 0

users_db: dict[int, Dict] = {}
user_id_counter = 0

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config["SECRET_KEY"], algorithm=config["ALGORITHM"])
    return encoded_jwt

def verify_token(credentials: HTTPAuthCredentials = Security(security)) -> TokenData:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, config["SECRET_KEY"], algorithms=[config["ALGORITHM"]])
        user_id: int = payload.get("user_id")
        username: str = payload.get("username")
        if user_id is None or username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
        token_data = TokenData(user_id=user_id, username=username)
        return token_data
    except JWTError:
        logger.error("JWT validation failed", extra={"token": token[:20]})
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

def log_request(endpoint: str, method: str, user_id: Optional[int] = None):
    logger.info("Request", extra={
        "endpoint": endpoint,
        "method": method,
        "user_id": user_id,
        "timestamp": datetime.now().isoformat()
    })

@app.get("/", tags=["root"])
@limiter.limit("100/minute")
async def read_root(request):
    log_request("/", "GET")
    return {"message": "Task Management API", "version": "2.0.0"}

@app.post("/auth/register", response_model=User, status_code=status.HTTP_201_CREATED, tags=["auth"])
@limiter.limit("5/minute")
async def register(request, user: UserCreate):
    global user_id_counter
    log_request("/auth/register", "POST")

    if any(u["username"] == user.username for u in users_db.values()):
        logger.warning("Registration failed - username already exists", extra={"username": user.username})
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )

    user_id_counter += 1
    new_user = {
        "id": user_id_counter,
        "username": user.username,
        "email": user.email,
        "hashed_password": hash_password(user.password)
    }
    users_db[user_id_counter] = new_user
    logger.info("User registered", extra={"user_id": user_id_counter, "username": user.username})
    return User(id=user_id_counter, username=user.username, email=user.email)

@app.post("/auth/login", response_model=Token, tags=["auth"])
@limiter.limit("10/minute")
async def login(request, credentials: UserLogin):
    log_request("/auth/login", "POST", extra={"username": credentials.username})

    user = None
    for u in users_db.values():
        if u["username"] == credentials.username:
            user = u
            break

    if not user or not verify_password(credentials.password, user["hashed_password"]):
        logger.warning("Login failed - invalid credentials", extra={"username": credentials.username})
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    access_token_expires = timedelta(minutes=config["ACCESS_TOKEN_EXPIRE_MINUTES"])
    access_token = create_access_token(
        data={"user_id": user["id"], "username": user["username"]},
        expires_delta=access_token_expires
    )
    logger.info("Login successful", extra={"user_id": user["id"], "username": user["username"]})
    return Token(
        access_token=access_token,
        expires_in=config["ACCESS_TOKEN_EXPIRE_MINUTES"] * 60
    )

@app.get("/tasks", response_model=List[Task], tags=["tasks"])
@limiter.limit("30/minute")
async def list_tasks(request, token_data: TokenData = Depends(verify_token), completed: Optional[bool] = None):
    log_request("/tasks", "GET", token_data.user_id)

    tasks = [t for t in tasks_db.values() if t.user_id == token_data.user_id]
    if completed is not None:
        tasks = [t for t in tasks if t.completed == completed]
    return tasks

@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["tasks"])
@limiter.limit("20/minute")
async def create_task(request, task: TaskCreate, token_data: TokenData = Depends(verify_token)):
    global task_id_counter
    log_request("/tasks", "POST", token_data.user_id)

    task_id_counter += 1
    now = datetime.now()
    new_task = Task(
        id=task_id_counter,
        title=task.title,
        description=task.description,
        completed=False,
        created_at=now,
        updated_at=now,
        user_id=token_data.user_id
    )
    tasks_db[task_id_counter] = new_task
    logger.info("Task created", extra={"task_id": task_id_counter, "user_id": token_data.user_id})
    return new_task

@app.get("/tasks/{task_id}", response_model=Task, tags=["tasks"])
@limiter.limit("30/minute")
async def get_task(request, task_id: int, token_data: TokenData = Depends(verify_token)):
    log_request(f"/tasks/{task_id}", "GET", token_data.user_id)

    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    task = tasks_db[task_id]
    if task.user_id != token_data.user_id:
        logger.warning("Unauthorized task access", extra={"task_id": task_id, "user_id": token_data.user_id})
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied"
        )
    return task

@app.put("/tasks/{task_id}", response_model=Task, tags=["tasks"])
@limiter.limit("20/minute")
async def update_task(request, task_id: int, task: TaskUpdate, token_data: TokenData = Depends(verify_token)):
    log_request(f"/tasks/{task_id}", "PUT", token_data.user_id)

    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    existing_task = tasks_db[task_id]
    if existing_task.user_id != token_data.user_id:
        logger.warning("Unauthorized task update", extra={"task_id": task_id, "user_id": token_data.user_id})
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied"
        )

    if task.title is not None:
        existing_task.title = task.title
    if task.description is not None:
        existing_task.description = task.description
    if task.completed is not None:
        existing_task.completed = task.completed

    existing_task.updated_at = datetime.now()
    tasks_db[task_id] = existing_task
    logger.info("Task updated", extra={"task_id": task_id, "user_id": token_data.user_id})
    return existing_task

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["tasks"])
@limiter.limit("20/minute")
async def delete_task(request, task_id: int, token_data: TokenData = Depends(verify_token)):
    log_request(f"/tasks/{task_id}", "DELETE", token_data.user_id)

    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    task = tasks_db[task_id]
    if task.user_id != token_data.user_id:
        logger.warning("Unauthorized task deletion", extra={"task_id": task_id, "user_id": token_data.user_id})
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied"
        )

    del tasks_db[task_id]
    logger.info("Task deleted", extra={"task_id": task_id, "user_id": token_data.user_id})
    return None

@app.get("/tasks/stats/summary", tags=["stats"])
@limiter.limit("30/minute")
async def get_stats(request, token_data: TokenData = Depends(verify_token)):
    log_request("/tasks/stats/summary", "GET", token_data.user_id)

    user_tasks = [t for t in tasks_db.values() if t.user_id == token_data.user_id]
    total = len(user_tasks)
    completed = sum(1 for t in user_tasks if t.completed)
    pending = total - completed
    return {
        "total": total,
        "completed": completed,
        "pending": pending
    }

@app.get("/health", tags=["health"])
@limiter.limit("100/minute")
async def health_check(request):
    logger.info("Health check", extra={"status": "ok"})
    return {"status": "healthy", "version": "2.0.0"}

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request, exc):
    logger.warning("Rate limit exceeded", extra={"path": str(request.url.path)})
    return {
        "error": "Rate limit exceeded",
        "detail": "Too many requests. Please try again later."
    }, status.HTTP_429_TOO_MANY_REQUESTS
