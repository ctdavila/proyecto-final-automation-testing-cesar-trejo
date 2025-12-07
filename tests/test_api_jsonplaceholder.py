import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


# ---------------------------------------------------------
# TEST 1 — GET: Obtener un post y validar estructura
# ---------------------------------------------------------
def test_get_post_by_id():
    response = requests.get(f"{BASE_URL}/posts/1")

    # Validar estado HTTP
    assert response.status_code == 200

    data = response.json()

    # Validar estructura esperada
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data

    # Validar contenido
    assert data["id"] == 1
    assert isinstance(data["title"], str)
    assert len(data["body"]) > 0



# ---------------------------------------------------------
# TEST 2 — POST: Crear un recurso (fake, pero JSONPlaceholder simula)
# ---------------------------------------------------------
def test_create_post():
    payload = {
        "title": "Mi post automatizado",
        "body": "Contenido de prueba",
        "userId": 99
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    # Validar estado HTTP simulado (siempre devuelve 201)
    assert response.status_code == 201

    data = response.json()

    # Validar lo que vuelve
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

    # JSONPlaceholder simula id generado
    assert "id" in data
    assert isinstance(data["id"], int)



# ---------------------------------------------------------
# TEST 3 — DELETE: Eliminar un post
# ---------------------------------------------------------
def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")

    # JSONPlaceholder devuelve 200 siempre
    assert response.status_code == 200

    # Puede devolver objeto vacío {}, lo validamos
    try:
        data = response.json()
        assert isinstance(data, dict)
    except:
        # Si no vuelve JSON, igual está ok para esta API
        assert True

