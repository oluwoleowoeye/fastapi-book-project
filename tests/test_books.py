from fastapi.testclient import TestClient
from main import app  # Ensure you import the FastAPI app

client = TestClient(app)


def test_get_all_books():
    response = client.get("/api/v1/books/")
    assert response.status_code == 200
    assert len(response.json()) == 3  # Adjust if your API has a different number of books


def test_get_single_book():
    response = client.get("/api/v1/books/1")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "The Great Gatsby"
    assert data["author"] == "F. Scott Fitzgerald"


def test_create_book():
    new_book = {
        "book_id": 4,
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
    }
    response = client.post("/api/v1/books/", json=new_book)
    assert response.status_code == 201
    data = response.json()
    assert data["book_id"] == 4
    assert data["title"] == "Harry Potter and the Sorcerer's Stone"


def test_update_book():
    updated_book = {
        "book_id": 1,
        "title": "The Great Gatsby: Updated Edition",
        "author": "F. Scott Fitzgerald",
    }
    response = client.put("/api/v1/books/1", json=updated_book)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "The Great Gatsby: Updated Edition"


def test_delete_book():
    response = client.delete("/api/v1/books/3")
    assert response.status_code == 204

    response = client.get("/api/v1/books/3")
    assert response.status_code == 404
