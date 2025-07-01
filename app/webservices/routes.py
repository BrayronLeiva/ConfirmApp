from fastapi import APIRouter
from app.webservices.user_web_service import router as user_router
from app.webservices.session_web_service import router as session_router
from app.webservices.attendance_web_service import router as attendance_router
from app.webservices.avatar_web_service import router as avatar_router

router = APIRouter()
router.include_router(user_router)
router.include_router(session_router)
router.include_router(attendance_router)
router.include_router(avatar_router)
