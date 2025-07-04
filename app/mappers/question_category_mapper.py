from app.entities.question_category import QuestionCategory    
from app.dtos.question_category_dtos import QuestionCategoryDTO


def question_category_dto_to_category_entity(dto: QuestionCategoryDTO) -> QuestionCategory:
    return QuestionCategory(
        name=dto.name,
        game_type=dto.game_type,
        is_active=dto.is_active
    )