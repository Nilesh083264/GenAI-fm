from fastapi import APIRouter
from api.controller_apis.user_router import router as user

router = APIRouter()


router.include_router(user)
