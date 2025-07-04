
from sqlalchemy.orm import Session
from app.entities.game_question import GameQuestion
from app.dtos.game_question_dtos import GameQuestionDTO, GameQuestionCreateDTO
from typing import Optional
from app.repositories.game_question_repository import GameQuestionRepository
from app.mappers.game_question_mapper import create_game_question_entity
from fastapi import HTTPException

class GameQuestionService:

    @staticmethod
    def get_all(db: Session) -> list[GameQuestionDTO]:
        questions = GameQuestionRepository.find_all(db)
        return [GameQuestionDTO.model_validate(q) for q in questions]

    
    @staticmethod
    def create_question(db: Session, dto: GameQuestionCreateDTO) -> GameQuestionDTO:
        entity = create_game_question_entity(dto)
        saved_entity = GameQuestionRepository.save(db, entity)
        return GameQuestionDTO.model_validate(saved_entity)

    @staticmethod
    def get_questions_by_category(
        db: Session,
        category_id: int
    ) -> list[GameQuestionDTO]:
        questions = GameQuestionRepository.find_by_category(db, category_id)
        return [GameQuestionDTO.model_validate(q) for q in questions]
