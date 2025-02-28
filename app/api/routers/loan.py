from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from app.config.database import get_db
from app.models.domains.loans import Loan
from app.schema.loans import LoanCreate, LoanResponse

router = APIRouter(prefix="/loans", tags=["loans"])

@router.get("/", response_model=List[LoanResponse])
async def get_loans(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Loan))
    return result.scalars().all()

@router.post("/", response_model=LoanResponse)
async def create_loan(loan: LoanCreate, db: AsyncSession = Depends(get_db)):
    db_loan = Loan(**loan.model_dump())
    db.add(db_loan)
    await db.commit()
    await db.refresh(db_loan)
    return db_loan

@router.delete("/{loan_id}")
async def delete_loan(loan_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Loan).where(Loan.id == loan_id))
    loan = result.scalar_one_or_none()
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    await db.delete(loan)
    await db.commit()
    return {"message": "Loan deleted successfully"}