from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from api.router import api_router
from core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_PREFIX)



@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}


# Define a Pydantic model for the Book response
class Book(BaseModel):
    book_id: int
    title: str
    author: str


# Sample book data
BOOKS_DB = {
    1: {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    2: {"title": "1984", "author": "George Orwell"},
    3: {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
}


@app.get("/api/v1/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    """Fetch a book by its ID and return as JSON. Returns 404 if book is not found."""
    book = BOOKS_DB.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return {"book_id": book_id, **book}  # ✅ Corrected response format
