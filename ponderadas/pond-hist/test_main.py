from fastapi.testclient import TestClient

from main import app

from random import randint

client = TestClient(app)

def test_get_historys():
    response = client.get("/hist/")
    assert response.status_code == 200

def test_write_history():
    response = client.post(
        "/hist/env",
        json={"conteudo": "Sou um bolo e quero ganhar a vida"})
    
    assert response.status_code == 200

def test_get_users():
    response = client.get("/users/")
    
    assert response.status_code == 200

def test_create_user():
    response = client.post(
        "/users/",
        json={"Email": f"test@example{randint(0, 1000)}.com", "password": "test"})
    assert response.status_code == 200

def test_login():
    response = client.post(
        "users/login",
        json={"Email": "test@example.com", "password": "test"}
    )
    assert response.status_code == 200