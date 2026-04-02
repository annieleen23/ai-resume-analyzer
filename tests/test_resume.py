from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_analyze_empty_resume():
    response = client.post("/api/v1/analyze", json={"resume_text": ""})
    assert response.status_code == 400


def test_analyze_returns_job_id():
    response = client.post("/api/v1/analyze", json={
        "resume_text": "John Doe, Software Engineer, Python, 3 years experience"
    })
    assert response.status_code == 200
    assert "job_id" in response.json()


def test_get_invalid_job():
    response = client.get("/api/v1/results/nonexistent-id")
    assert response.status_code == 404
