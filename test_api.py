import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_db():
    from main import tasks_db, users_db, task_id_counter, user_id_counter
    tasks_db.clear()
    users_db.clear()
    yield

def get_auth_headers(username: str, password: str, email: str) -> dict:
    client.post(
        "/auth/register",
        json={"username": username, "password": password, "email": email}
    )

    response = client.post(
        "/auth/login",
        json={"username": username, "password": password}
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["version"] == "2.0.0"

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_register_user():
    response = client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "password": "password123",
            "email": "test@example.com"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_register_duplicate_username():
    client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "password": "password123",
            "email": "test@example.com"
        }
    )

    response = client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "password": "password456",
            "email": "test2@example.com"
        }
    )
    assert response.status_code == 400
    assert "already registered" in response.json()["detail"]

def test_login():
    client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "password": "password123",
            "email": "test@example.com"
        }
    )

    response = client.post(
        "/auth/login",
        json={"username": "testuser", "password": "password123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert data["expires_in"] > 0

def test_login_invalid_password():
    client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "password": "password123",
            "email": "test@example.com"
        }
    )

    response = client.post(
        "/auth/login",
        json={"username": "testuser", "password": "wrongpassword"}
    )
    assert response.status_code == 401

def test_login_user_not_found():
    response = client.post(
        "/auth/login",
        json={"username": "nonexistent", "password": "password123"}
    )
    assert response.status_code == 401

def test_create_task_requires_auth():
    response = client.post(
        "/tasks",
        json={"title": "Test Task"}
    )
    assert response.status_code == 403

def test_create_task_with_auth():
    headers = get_auth_headers("testuser", "password123", "test@example.com")

    response = client.post(
        "/tasks",
        json={"title": "Test Task", "description": "Test Description"},
        headers=headers
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["user_id"] == 1

def test_create_task_without_description():
    headers = get_auth_headers("testuser", "password123", "test@example.com")

    response = client.post(
        "/tasks",
        json={"title": "Task without description"},
        headers=headers
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Task without description"
    assert data["description"] is None

def test_create_task_invalid_title():
    headers = get_auth_headers("testuser", "password123", "test@example.com")

    response = client.post(
        "/tasks",
        json={"title": ""},
        headers=headers
    )
    assert response.status_code == 422

def test_list_tasks_requires_auth():
    response = client.get("/tasks")
    assert response.status_code == 403

def test_list_tasks_user_isolation():
    headers1 = get_auth_headers("user1", "password123", "user1@example.com")
    headers2 = get_auth_headers("user2", "password123", "user2@example.com")

    client.post(
        "/tasks",
        json={"title": "User1 Task"},
        headers=headers1
    )
    client.post(
        "/tasks",
        json={"title": "User2 Task"},
        headers=headers2
    )

    response = client.get("/tasks", headers=headers1)
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["user_id"] == 1

    response = client.get("/tasks", headers=headers2)
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["user_id"] == 2

def test_get_task():
    headers = get_auth_headers("testuser", "password123", "test@example.com")

    create_response = client.post(
        "/tasks",
        json={"title": "Get Task Test"},
        headers=headers
    )
    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == "Get Task Test"

def test_get_task_not_found():
    headers = get_auth_headers("testuser", "password123", "test@example.com")

    response = client.get("/tasks/99999", headers=headers)
    assert response.status_code == 404

def test_get_task_forbidden():
    headers1 = get_auth_headers("user1", "password123", "user1@example.com")
    headers2 = get_auth_headers("user2", "password123", "user2@example.com")

    create_response = client.post(
        "/tasks",
        json={"title": "User1 Task"},
        headers=headers1
    )
    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}", headers=headers2)
    assert response.status_code == 403

def test_update_task():
    headers = get_auth_headers("testuser", "password123", "test@example.com")

    create_response = client.post(
        "/tasks",
        json={"title": "Original Title", "description": "Original"},
        headers=headers
    )
    task_id = create_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={"title": "Updated Title", "completed": True},
        headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["completed"] is True
    assert data["description"] == "Original"

def test_update_task_partial():
    headers = get_auth_headers("testuser", "password123", "test@example.com")

    create_response = client.post(
        "/tasks",
        json={"title": "Task", "description": "Description"},
        headers=headers
    )
    task_id = create_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={"completed": True},
        headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["completed"] is True
    assert data["title"] == "Task"

def test_update_task_forbidden():
    headers1 = get_auth_headers("user1", "password123", "user1@example.com")
    headers2 = get_auth_headers("user2", "password123", "user2@example.com")

    create_response = client.post(
        "/tasks",
        json={"title": "User1 Task"},
        headers=headers1
    )
    task_id = create_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={"completed": True},
        headers=headers2
    )
    assert response.status_code == 403

def test_delete_task():
    headers = get_auth_headers("testuser", "password123", "test@example.com")

    create_response = client.post(
        "/tasks",
        json={"title": "Task to Delete"},
        headers=headers
    )
    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}", headers=headers)
    assert response.status_code == 204

    response = client.get(f"/tasks/{task_id}", headers=headers)
    assert response.status_code == 404

def test_delete_task_forbidden():
    headers1 = get_auth_headers("user1", "password123", "user1@example.com")
    headers2 = get_auth_headers("user2", "password123", "user2@example.com")

    create_response = client.post(
        "/tasks",
        json={"title": "User1 Task"},
        headers=headers1
    )
    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}", headers=headers2)
    assert response.status_code == 403

def test_filter_tasks_by_completion():
    headers = get_auth_headers("testuser", "password123", "test@example.com")

    client.post("/tasks", json={"title": "Pending Task"}, headers=headers)
    response = client.post("/tasks", json={"title": "Task to Complete"}, headers=headers)
    task_id = response.json()["id"]

    client.put(f"/tasks/{task_id}", json={"completed": True}, headers=headers)

    response = client.get("/tasks?completed=true", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) >= 1

    response = client.get("/tasks?completed=false", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) >= 1

def test_get_stats():
    headers = get_auth_headers("testuser", "password123", "test@example.com")

    client.post("/tasks", json={"title": "Task 1"}, headers=headers)
    client.post("/tasks", json={"title": "Task 2"}, headers=headers)
    response = client.post("/tasks", json={"title": "Task 3"}, headers=headers)
    task_id = response.json()["id"]

    client.put(f"/tasks/{task_id}", json={"completed": True}, headers=headers)

    response = client.get("/tasks/stats/summary", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 3
    assert data["completed"] == 1
    assert data["pending"] == 2

def test_invalid_token():
    response = client.get(
        "/tasks",
        headers={"Authorization": "Bearer invalid_token"}
    )
    assert response.status_code == 401
