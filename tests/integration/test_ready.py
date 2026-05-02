from fastapi.testclient import TestClient

from src.api.main import app


def test_ready_endpoint_exists():
    client = TestClient(app)
    response = client.get('/ready')
    assert response.status_code == 200
    assert 'status' in response.json()
