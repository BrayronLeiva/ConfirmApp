from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from app.dtos.user_role import UserRole

class UserCreateDTO(BaseModel):
    name: str
    username: str
    password: str

class UserResponseDTO(BaseModel):
    id: int
    name: str
    username: str
    avatar_url: Optional[str] = None
    total_points: int
    rol: UserRole

    model_config = ConfigDict(from_attributes=True)