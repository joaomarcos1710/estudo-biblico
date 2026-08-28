from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Task Management API", version="1.0.0")

class Task(BaseModel):
    id: int
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    completed: bool = False
    created_at: datetime
    updated_at: datetime

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    completed: Optional[bool] = None

tasks_db: dict[int, Task] = {}
task_id_counter = 0

@app.get("/", tags=["root"])
def read_root():
    return {"message": "Task Management API", "version": "1.0.0"}

@app.get("/tasks", response_model=List[Task], tags=["tasks"])
def list_tasks(completed: Optional[bool] = None):
    tasks = list(tasks_db.values())
    if completed is not None:
        tasks = [t for t in tasks if t.completed == completed]
    return tasks

@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["tasks"])
def create_task(task: TaskCreate):
    global task_id_counter
    task_id_counter += 1
    now = datetime.now()
    new_task = Task(
        id=task_id_counter,
        title=task.title,
        description=task.description,
        completed=False,
        created_at=now,
        updated_at=now
    )
    tasks_db[task_id_counter] = new_task
    return new_task

@app.get("/tasks/{task_id}", response_model=Task, tags=["tasks"])
def get_task(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    return tasks_db[task_id]

@app.put("/tasks/{task_id}", response_model=Task, tags=["tasks"])
def update_task(task_id: int, task: TaskUpdate):
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    existing_task = tasks_db[task_id]
    if task.title is not None:
        existing_task.title = task.title
    if task.description is not None:
        existing_task.description = task.description
    if task.completed is not None:
        existing_task.completed = task.completed

    existing_task.updated_at = datetime.now()
    tasks_db[task_id] = existing_task
    return existing_task

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["tasks"])
def delete_task(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    del tasks_db[task_id]
    return None

@app.get("/tasks/stats/summary", tags=["stats"])
def get_stats():
    total = len(tasks_db)
    completed = sum(1 for t in tasks_db.values() if t.completed)
    pending = total - completed
    return {
        "total": total,
        "completed": completed,
        "pending": pending
    }
