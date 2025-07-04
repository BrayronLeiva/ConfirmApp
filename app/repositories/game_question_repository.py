
from sqlalchemy.orm import Session
from app.entities.game_question import GameQuestion
from typing import Optional

class GameQuestionRepository:

    @staticmethod
    def find_all(db: Session) -> list[GameQuestion]:
        return db.query(GameQuestion).all()


    @staticmethod
    def save(db: Session, entity: GameQuestion) -> GameQuestion:
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity
    
    @staticmethod
    def find_by_category(
        db: Session,
        category_id: int
    ) -> list[GameQuestion]:
        return db.query(GameQuestion).filter(GameQuestion.category_id == category_id).all()

