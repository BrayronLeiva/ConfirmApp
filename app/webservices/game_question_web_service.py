from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.services.game_question_service import GameQuestionService
from app.dtos.game_question_dtos import GameQuestionDTO, GameQuestionCreateDTO
from typing import Optional

router = APIRouter(prefix="/v1/game-questions", tags=["game-questions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("", response_model=list[GameQuestionDTO])
def get_all_questions(db: Session = Depends(get_db)):
    return GameQuestionService.get_all(db)

@router.post("", response_model=GameQuestionDTO)
def create_question(dto: GameQuestionCreateDTO, db: Session = Depends(get_db)):
    return GameQuestionService.create_question(db, dto)

@router.get("/categories/{category_id}", response_model=list[GameQuestionDTO])
def get_questions_by_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    return GameQuestionService.get_questions_by_category(db, category_id)
