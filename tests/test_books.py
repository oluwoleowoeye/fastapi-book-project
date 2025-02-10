import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_single_book():
    response = client.get("/api/v1/books/1")  # ✅ Ensure book ID exists
    assert response.status_code == 200
    
    data = response.json()
    assert data["book_id"] == 1
    assert data["title"] == "The Great Gatsby"
    assert data["author"] == "F. Scott Fitzgerald"


def test_get_nonexistent_book():
    response = client.get("/api/v1/books/999")  # ✅ Non-existent book
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}
