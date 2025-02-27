from sqlalchemy import Column,Integer,String
from app.config.database import Base

class Book(Base):
    __tablename__="books"

    id=Column(Integer,primary_key=True,index=True)
    book_name=Column(String,nullable=False)
    isbn=Column(Integer,nullable=False)
    author=Column(String,nullable=False)