"""Module to initialize env variables"""
from dotenv import load_dotenv
from pydantic import BaseSettings
from pymongo import MongoClient

load_dotenv()


class Settings(BaseSettings):
    """Class that initializes env variables"""

    MONGO_URI: str

    @property
    def mongo_client(self):
        """Starts Mongo connection."""
        client = MongoClient(self.MONGO_URI)
        return client

    class Config:
        """Set env file"""

        env_file = ".env"
