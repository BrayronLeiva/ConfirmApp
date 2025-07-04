from typing import Optional
from app.dtos.question_category_dtos import QuestionCategoryDTO, QuestionCategoryCreateDTO
from app.dtos.game_question_dtos import GameQuestionDTO
from app.entities.question_category import QuestionCategory
from app.repositories.question_category_repository import QuestionCategoryRepository
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.mappers.question_category_mapper import question_category_dto_to_category_entity


class QuestionCategoryService:

    @staticmethod
    def get_categories(db: Session, is_active: Optional[bool] = None) -> list[QuestionCategoryDTO]:
        entities = QuestionCategoryRepository.find_all(db, is_active)
        return [QuestionCategoryDTO.model_validate(c) for c in entities]

    @staticmethod
    def create_category(db: Session, dto: QuestionCategoryCreateDTO) -> QuestionCategoryDTO:
        entity = question_category_dto_to_category_entity(dto)
        entity = QuestionCategoryRepository.create(db, entity)
        return QuestionCategoryDTO.model_validate(entity)
