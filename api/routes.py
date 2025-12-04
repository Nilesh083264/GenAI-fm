from fastapi import APIRouter
from api.controller_apis.sai import router as Hello_sai_api
from api.controller_apis.nilesh import router as nilesh_api
from api.controller_apis.user_router import router as user

router = APIRouter()


router.include_router(Hello_sai_api)
router.include_router(nilesh_api)
router.include_router(user)
