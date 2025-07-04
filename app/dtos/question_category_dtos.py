from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class QuestionCategoryDTO(BaseModel):
    id: Optional[int]
    name: str
    game_type: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class QuestionCategoryCreateDTO(BaseModel):
    name: str
    game_type: str
    is_active: bool