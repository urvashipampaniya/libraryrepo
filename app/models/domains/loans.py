from sqlalchemy import Column, Integer,String, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from app.config.database import Base
from datetime import datetime



class Loan(Base):
    __tablename__="loan"

    id=Column(Integer,primary_key=True,index=True)
    books_id=Column(Integer,ForeignKey("books.id"))
    person_id = Column(Integer, ForeignKey("member.id"))  
    loan_date=Column(DateTime, default=datetime.now)
    return_date=Column(DateTime, default=datetime.now)

    book=relationship("Book")
    member=relationship("Member")
