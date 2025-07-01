from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from app.dtos.user_role import UserRole
from app.dtos.avatar_dtos import AvatarResponseDTO
class UserCreateDTO(BaseModel):
    name: str
    username: str
    password: str

class UserResponseDTO(BaseModel):
    id: int
    name: str
    username: str
    total_points: int
    rol: UserRole
    avatar: Optional[AvatarResponseDTO] = None

    model_config = ConfigDict(from_attributes=True)


class AuthRequestDTO(BaseModel):
    username: str
    password: str

class AuthResponseDTO(BaseModel):
    access_token: str
    #token_type: str = "bearer"
    user_id: int