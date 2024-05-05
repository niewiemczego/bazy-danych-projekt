from uuid import UUID, uuid4

from fastapi import FastAPI
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str
    author: str
    description: str
    rating: int


class BookRequest(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(min_length=3)
    author: str = Field(min_length=5)
    description: str = Field(min_length=10)
    rating: int = Field(ge=1, le=5)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "description": "The story of the mysteriously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan.",
                "rating": 3,
            }
        }


BOOKS = [
    Book(
        id=uuid4(),
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        description="The story of the mysteriously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan.",
        rating=3,
    ),
    Book(
        id=uuid4(),
        title="To Kill a Mockingbird",
        author="Harper Lee",
        description="The story of a young girl named Scout growing up in the South during the 1930s.",
        rating=4,
    ),
    Book(
        id=uuid4(),
        title="1984 - Nineteen Eighty-Four",
        author="George Orwell",
        description="A dystopian novel set in a totalitarian society.",
        rating=3,
    ),
]


@app.get("/books", response_model=list[Book], status_code=status.HTTP_200_OK)
def get_all_books() -> list[Book]:
    return BOOKS


@app.post("/books", response_model=Book)
def create_book(book_request: BookRequest) -> Book:
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)
    return new_book
