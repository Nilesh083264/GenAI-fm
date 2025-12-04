from repositories.user_repository import UserRepository
from services.base_service import BaseService

class UserService(BaseService):

    @staticmethod
    async def create_user(data: dict):
        try:
            created_user = await UserRepository.create(data)
            return UserService.format_response(created_user, "User created successfully")
        except Exception as e:
            return UserService.format_error(str(e))

    @staticmethod
    async def list_users():
        try:
            users = await UserRepository.get_all()
            return UserService.format_response(users, "Users fetched successfully")
        except Exception as e:
            return UserService.format_error(str(e))

    @staticmethod
    async def get_user(user_id: str):
        try:
            user = await UserRepository.get_by_id(user_id)
            if not user:
                return UserService.format_error("User not found")
            return UserService.format_response(user, "User fetched successfully")
        except Exception as e:
            return UserService.format_error(str(e))
