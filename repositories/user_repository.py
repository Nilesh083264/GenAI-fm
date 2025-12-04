from database.connection import db
from database.config import USERS_COLLECTION
from bson import ObjectId
from repositories.base_repository import BaseRepository

class UserRepository(BaseRepository):

    @staticmethod
    async def create(user: dict):
        result = await db[USERS_COLLECTION].insert_one(user)
        user["_id"] = result.inserted_id
        return UserRepository.convert_object_id(user)

    @staticmethod
    async def get_all():
        users = await db[USERS_COLLECTION].find().to_list(100)
        return UserRepository.convert_object_id(users)

    @staticmethod
    async def get_by_id(user_id: str):
        user = await db[USERS_COLLECTION].find_one({"_id": ObjectId(user_id)})
        return UserRepository.convert_object_id(user) if user else None
