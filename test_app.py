from app import app

def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Task Management System" in response.data

def test_add_task():
    client = app.test_client()
    response = client.post("/add", data={"title": "Study DevOps"})
    assert response.status_code == 302
    assert len(response.data) >= 0

def test_empty_task_not_added():
    import app as application
    before = len(application.tasks)
    client = app.test_client()
    client.post("/add", data={"title": "   "})
    assert len(application.tasks) == before
