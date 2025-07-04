from sqlalchemy.orm import Session
from app.entities.game_question import GameQuestion
from app.dtos.game_question_dtos import GameQuestionDTO


def create_game_question_entity(dto: GameQuestionDTO) -> GameQuestion:
    return GameQuestion(
        question_text=dto.question_text,
        option_a=dto.option_a,
        option_b=dto.option_b,
        option_c=dto.option_c,
        option_d=dto.option_d,
        correct_answer=dto.correct_answer,
        category_id=dto.category_id
    )
