from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_hc_main():
    response = client.get("/hc")
    assert response.status_code == 200
    assert response.json() == {"Health - OK"}

def test_logwarning_main():
    response = client.get("/logwarning")
    assert response.status_code == 200

def test_logerror_main():
    response = client.get("/logerror")
    assert response.status_code == 200

def test_logdebug_main():
    response = client.get("/logdebug")
    assert response.status_code == 200
