from sqlalchemy.orm import Session
from typing import List, Optional
from app.entities.question_category import QuestionCategory
from app.entities.game_question import GameQuestion

class QuestionCategoryRepository:

    @staticmethod
    def find_all(db: Session, is_active: Optional[bool] = None) -> List[QuestionCategory]:
        query = db.query(QuestionCategory)
        if is_active is not None:
            query = query.filter(QuestionCategory.is_active == is_active)
        return query.all()

    @staticmethod
    def get_by_id(db: Session, category_id: int) -> Optional[QuestionCategory]:
        return db.query(QuestionCategory).filter(QuestionCategory.id == category_id).first()

    @staticmethod
    def create(db: Session, entity: QuestionCategory) -> QuestionCategory:
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity