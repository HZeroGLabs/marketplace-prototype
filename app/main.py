from app.db.database import engine, Base
from app.routers import users
from app.routers import listings
from fastapi import FastAPI
from app.models import user
from app.models import listings as listings_model

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(users.router)
app.include_router(listings.router)

@app.get("/")
def read_root():
    return {"status": "Marketplace prototype is running!"}