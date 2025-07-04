
from pydantic import BaseModel, ConfigDict
from typing import Optional

class GameQuestionDTO(BaseModel):
    id: Optional[int]
    question_text: str
    option_a: Optional[str] = None
    option_b: Optional[str] = None
    option_c: Optional[str] = None
    option_d: Optional[str] = None
    correct_answer: str  # Ej: "A", "B", etc.
    category_id: int

    model_config = ConfigDict(from_attributes=True)

class GameQuestionCreateDTO(BaseModel):
    question_text: str
    option_a: Optional[str] = None
    option_b: Optional[str] = None
    option_c: Optional[str] = None
    option_d: Optional[str] = None
    correct_answer: str  # Ej: "A", "B", etc.
    category_id: int


