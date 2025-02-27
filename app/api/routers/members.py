from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from app.config.database import get_db
from app.models.domains.members import Member
from app.schema.members import MemberCreate, MemberResponse

router = APIRouter()

@router.get("/", response_model=List[MemberResponse])
async def get_members(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Member))
    return result.scalars().all()

@router.post("/", response_model=MemberResponse)
async def create_member(member: MemberCreate, db: AsyncSession = Depends(get_db)):
    db_member = Member(**member.model_dump())
    db.add(db_member)
    await db.commit()
    await db.refresh(db_member)
    return db_member

@router.delete("/{member_id}")
async def delete_member(member_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Member).where(Member.id == member_id))
    member = result.scalar_one_or_none()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    await db.delete(member)
    await db.commit()
    return {"message": "Member deleted successfully"}