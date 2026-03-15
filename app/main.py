from app.db.database import engine, Base
from app.routers import users
from fastapi import FastAPI
from app.models import user

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(users.router)

@app.get("/")
def read_root():
    return {"status": "Marketplace prototype is running!"}