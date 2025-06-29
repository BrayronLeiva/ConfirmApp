from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional



class AttendanceCreateDTO(BaseModel):
    user_id: int
    session_id: int

class AttendanceResponseDTO(BaseModel):
    id: int
    user_id: int
    session_id: int
    attended_at: datetime

    model_config = ConfigDict(from_attributes=True)
