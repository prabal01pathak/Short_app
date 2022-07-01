"""
Discription: Test short_app routes
Author: Prabal Pathak
"""
from fastapi.testclient import TestClient

from short_app import __version__
from short_app.app import app

client = TestClient(app)


def test_version():
    """test the application version"""
    assert __version__ == "0.1.0"


def test_root():
    """Test root route"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}
