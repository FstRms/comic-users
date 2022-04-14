"""Module that handles Mongo operations"""
from uuid import uuid4


class MongoHandler:
    """Class that handles Mongo operations"""

    def __init__(self, client):
        """Initialize class with MongoClient"""
        self.client = client
        self.db = client.comic_users
        self.collection = self.db.users

    def get_users(self) -> list:
        """Get all users"""
        data = self.collection.find()
        output = []
        for each in data:
            output.append(self.mapp_result(each))
        return output

    def register_user(self, name, password, age) -> str:
        """Register a new user"""
        token = uuid4()
        last_user = self.collection.find_one(sort=[("_id", -1)])
        new_id = last_user["id"] + 1 if last_user else 1
        payload = {
            "name": name,
            "password": password,
            "age": age,
            "token": token,
            "id": new_id,
        }
        insertion = self.collection.insert_one(payload)
        inserted_id = str(insertion.inserted_id)
        return inserted_id

    def login_user(self, name, password) -> dict:
        """Login a user"""
        user = self.db.users.find_one({"name": name, "password": password})
        return self.mapp_result(user)

    @staticmethod
    def mapp_result(user) -> dict:
        """Map result to a dict"""
        return {
            "name": user["name"],
            "age": user["age"],
            "token": user["token"],
            "id": user["id"],
        }
