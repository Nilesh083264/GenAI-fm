from fastapi import APIRouter
from pydantic import BaseModel
from services.user_service import UserService

router = APIRouter()

class User(BaseModel):
    name: str
    email: str

@router.post("/users")
async def create_user(user: User):
    return await UserService.create_user(user.dict())

@router.get("/users")
async def list_users():
    return await UserService.list_users()

@router.get("/users/{user_id}")
async def get_user(user_id: str):
    return await UserService.get_user(user_id)
