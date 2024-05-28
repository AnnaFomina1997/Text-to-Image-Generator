import pytest
from fastapi.testclient import TestClient
from Backend.app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Text to Image Generator" in response.text


def test_static_files():
    response = client.get("/static/css/style.css")
    assert response.status_code == 200

    response = client.get("/static/js/script.js")
    assert response.status_code == 200
