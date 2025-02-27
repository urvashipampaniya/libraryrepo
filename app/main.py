from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config.database import create_all_tables
from app.api.routers.books import router as books_router
from app.api.routers.members import router as members_router
from app.api.routers.loan import router as loans_router

@asynccontextmanager
async def lifespan(app: FastAPI):
   
    await create_all_tables()
    yield
    print("Application is shutting down...")

app = FastAPI(title="Library Management System", lifespan=lifespan)


app.include_router(books_router)
app.include_router(members_router)
app.include_router(loans_router)

