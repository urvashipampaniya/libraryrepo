from pydantic import BaseModel
from datetime import datetime

class BookBase(BaseModel):
    book_name: str
    isbn: int
    author: str

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True