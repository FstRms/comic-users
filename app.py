"""Main app Module"""

from functools import lru_cache

from fastapi import Depends, FastAPI

from src.config import Settings
from src.db import MongoHandler

app = FastAPI(
    title="Comic Users API",
    description="API that handles user data for comics store",
    version="0.1.0",
)


@lru_cache()
def get_settings():
    return Settings()


@app.get("/")
async def home_page():
    """Homepage"""

    return {"message": "Welcome to the Comic Users API"}


@app.get("/users")
def get_users(settings: Settings = Depends(get_settings)):
    """Get all users"""
    mongo_handler = MongoHandler(settings.mongo_client)
    data = mongo_handler.get_users()
    return data


@app.post("/register", status_code=201)
def register_user(
    name: str, password: str, age: int, settings: Settings = Depends(get_settings)
):
    """Register a new user"""
    mongo_handler = MongoHandler(settings.mongo_client)
    insertion = mongo_handler.register_user(name, password, age)
    return {"message": "User registered", "inserted_id": insertion}


@app.post("/login")
def login_user(name: str, password: str, settings: Settings = Depends(get_settings)):
    """Login a user"""
    mongo_handler = MongoHandler(settings.mongo_client)
    data = mongo_handler.login_user(name, password)
    return data
