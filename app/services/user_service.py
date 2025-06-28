from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from fastapi import HTTPException
from app.dtos.users import UserCreateDTO, UserResponseDTO
from app.mappers.user_mapper import user_create_dto_to_entity
from app.repositories.user_repository import UserRepository
from app.config.security.jwt_utils import create_access_token

class UserService:

    @staticmethod
    def register(db: Session, dto: UserCreateDTO) -> UserResponseDTO:
        if UserRepository.get_by_username(db, dto.username):
            raise HTTPException(status_code=400, detail="Username ya registrado")
        
        user = user_create_dto_to_entity(dto)
        user = UserRepository.create(db, user)
        return UserResponseDTO.model_validate(user)


    @staticmethod
    def login(db: Session, username: str, password: str) -> str:
        user = UserRepository.get_by_username(db, username)

        if not user or not bcrypt.verify(password, user.password_hash):
            raise HTTPException(status_code=401, detail="Credenciales inválidas")
        return create_access_token({"sub": str(user.id), "rol": user.rol.value})
