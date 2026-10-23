from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_root_identifies_project():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["project"] == "Araç Forum Platformu"
