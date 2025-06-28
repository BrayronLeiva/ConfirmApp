from app.entities.user import User
from app.dtos.users import UserCreateDTO
from passlib.hash import bcrypt

def user_create_dto_to_entity(dto: UserCreateDTO) -> User:
    return User(
        name=dto.name,
        username=dto.username,
        password_hash=bcrypt.hash(dto.password),
    )
