from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from app.dtos.question_category_dtos import QuestionCategoryDTO, QuestionCategoryCreateDTO
from app.services.question_category_service import QuestionCategoryService
from app.config.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(prefix="/v1/questionCategory", tags=["questionCategory"])

@router.get("", response_model=list[QuestionCategoryDTO])
def get_categories(is_active: Optional[bool] = None, db: Session = Depends(get_db)):
    return QuestionCategoryService.get_categories(db, is_active)

@router.post("", response_model=QuestionCategoryDTO)
def create_category(dto: QuestionCategoryCreateDTO, db: Session = Depends(get_db)):
    return QuestionCategoryService.create_category(db, dto)