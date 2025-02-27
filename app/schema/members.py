from pydantic import BaseModel
from datetime import datetime

class MemberBase(BaseModel):
    name: str
    age: int
    email: str

class MemberCreate(MemberBase):
    pass

class MemberResponse(MemberBase):
    id: int

    class Config:
        from_attributes = True