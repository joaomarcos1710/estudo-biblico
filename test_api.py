import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Test Task", "description": "Test Description"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test Description"
    assert data["completed"] is False
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data

def test_create_task_without_description():
    response = client.post(
        "/tasks",
        json={"title": "Task without description"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Task without description"
    assert data["description"] is None

def test_create_task_invalid_title():
    response = client.post(
        "/tasks",
        json={"title": "", "description": "Test"}
    )
    assert response.status_code == 422

def test_list_tasks():
    client.post("/tasks", json={"title": "Task 1"})
    client.post("/tasks", json={"title": "Task 2"})

    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) >= 2

def test_get_task():
    create_response = client.post(
        "/tasks",
        json={"title": "Get Task Test"}
    )
    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == "Get Task Test"

def test_get_task_not_found():
    response = client.get("/tasks/99999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]

def test_update_task():
    create_response = client.post(
        "/tasks",
        json={"title": "Original Title", "description": "Original"}
    )
    task_id = create_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={"title": "Updated Title", "completed": True}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["completed"] is True
    assert data["description"] == "Original"

def test_update_task_partial():
    create_response = client.post(
        "/tasks",
        json={"title": "Task", "description": "Description"}
    )
    task_id = create_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={"completed": True}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["completed"] is True
    assert data["title"] == "Task"
    assert data["description"] == "Description"

def test_update_task_not_found():
    response = client.put(
        "/tasks/99999",
        json={"title": "Updated"}
    )
    assert response.status_code == 404

def test_delete_task():
    create_response = client.post(
        "/tasks",
        json={"title": "Task to Delete"}
    )
    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404

def test_delete_task_not_found():
    response = client.delete("/tasks/99999")
    assert response.status_code == 404

def test_filter_tasks_by_completion():
    client.post("/tasks", json={"title": "Pending Task"})
    response = client.post("/tasks", json={"title": "Task to Complete"})
    task_id = response.json()["id"]

    client.put(f"/tasks/{task_id}", json={"completed": True})

    response = client.get("/tasks?completed=true")
    assert response.status_code == 200
    assert len(response.json()) >= 1

    response = client.get("/tasks?completed=false")
    assert response.status_code == 200
    assert len(response.json()) >= 1

def test_get_stats():
    response = client.get("/tasks/stats/summary")
    assert response.status_code == 200
    data = response.json()
    assert "total" in data
    assert "completed" in data
    assert "pending" in data
    assert data["total"] == data["completed"] + data["pending"]
