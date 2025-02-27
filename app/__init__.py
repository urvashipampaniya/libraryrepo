from fastapi import FastAPI

app = FastAPI()

from app.api.routers import books, loan, members


app.include_router(books.router)
app.include_router(loan.router)
app.include_router(members.router)
