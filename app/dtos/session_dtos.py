from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class SessionCreateDTO(BaseModel):
    name: str
    summary: Optional[str]
    scheduled_at: datetime
    level: int
    qr_code: Optional[str]

class SessionResponseDTO(BaseModel):
    id: int
    name: str
    summary: Optional[str]
    scheduled_at: datetime
    level: int
    qr_code: Optional[str]

    model_config = ConfigDict(from_attributes=True)
