import requests
import pytest

# Uso JSONPlaceholder que es más permisiva y estable
BASE_URL = "https://jsonplaceholder.typicode.com"

# CASO 1: GET - Obtener un recurso existente
def test_get_post_status_200():
    response = requests.get(f"{BASE_URL}/posts/1")
    
    # Validaciones
    assert response.status_code == 200
    data = response.json()
    assert "userId" in data
    assert data["id"] == 1

# CASO 2: POST - Crear un recurso
def test_create_post_status_201():
    payload = {
        "title": "Automation Test",
        "body": "Este es un post de prueba",
        "userId": 1
    }
    
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    
    # JSONPlaceholder devuelve 201 cuando se crea algo
    assert response.status_code == 201
    
    # Validamos que la respuesta contenga el título que enviamos
    data = response.json()
    assert data["title"] == "Automation Test"
    assert "id" in data

# CASO 3: DELETE - Borrar un recurso
def test_delete_post_status_200():
    response = requests.delete(f"{BASE_URL}/posts/1")
    
    # JSONPlaceholder devuelve 200 (OK) al borrar, a diferencia de otros que dan 204
    assert response.status_code == 200
    
    # Validamos que devuelve un JSON vacío {}
    assert response.json() == {}