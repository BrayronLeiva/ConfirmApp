from fastapi import APIRouter
from app.webservices.user_web_service import router as user_router
from app.webservices.session_web_service import router as session_router

router = APIRouter()
router.include_router(user_router)
router.include_router(session_router)
