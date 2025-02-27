from sqlalchemy import Column,String,Integer
from app.config.database import Base

class Member(Base):
    __tablename__="member"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    age=Column(Integer,nullable=False)
    email=Column(String,nullable=False)
    
