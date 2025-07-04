from fastapi import APIRouter
from app.webservices.user_web_service import router as user_router
from app.webservices.session_web_service import router as session_router
from app.webservices.attendance_web_service import router as attendance_router
from app.webservices.avatar_web_service import router as avatar_router
from app.webservices.game_question_web_service import router as game_question_router
from app.webservices.question_category_web_service import router as question_category_router


router = APIRouter()
router.include_router(user_router)
router.include_router(session_router)
router.include_router(attendance_router)
router.include_router(avatar_router)
router.include_router(game_question_router)
router.include_router(question_category_router)