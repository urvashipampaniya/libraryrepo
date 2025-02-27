from pydantic import BaseModel
from datetime import datetime

class LoanBase(BaseModel):
    book_id: int
    member_id: int
    return_date: datetime

class LoanCreate(LoanBase):
    pass

class LoanResponse(LoanBase):
    id: int
    loan_date: datetime

    class Config:
        from_attributes = True