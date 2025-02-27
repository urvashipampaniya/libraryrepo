from fastapi import APIRouter

api_router = APIRouter()

from app.api.routers.books import router as books_router
from app.api.routers.loan import router as loans_router
from app.api.routers.members import router as members_router


api_router.include_router(books_router, prefix="/books", tags=["books"])
api_router.include_router(loans_router, prefix="/loans", tags=["loans"])
api_router.include_router(members_router, prefix="/members", tags=["members"])
