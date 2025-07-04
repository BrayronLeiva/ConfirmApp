from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from fastapi import HTTPException
from app.dtos.users import UserCreateDTO, UserResponseDTO, AuthRequestDTO, AuthResponseDTO, UserUpdateAvatarDto
from app.mappers.user_mapper import user_create_dto_to_entity
from app.repositories.user_repository import UserRepository
from app.config.security.jwt_utils import create_access_token
from app.dtos.user_role import UserRole
from app.dtos.users import UserUpdatePointsDto

class UserService:

    @staticmethod
    def register(db: Session, dto: UserCreateDTO) -> UserResponseDTO:
        
        if UserRepository.get_by_username(db, dto.username):
            raise HTTPException(status_code=400, detail="Username ya registrado")
        

        user = user_create_dto_to_entity(dto)
        user = UserRepository.create(db, user)
        return UserResponseDTO.model_validate(user)


    @staticmethod
    def login(db: Session, dto: AuthRequestDTO) -> AuthResponseDTO:
        user = UserRepository.get_by_username(db, dto.username)

        if not user or not bcrypt.verify(dto.password, user.password_hash):
            raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
        token = create_access_token({"sub": str(user.id), "rol": user.rol.value})
        return AuthResponseDTO(access_token=token, user_id=user.id)

    @staticmethod
    def get_user_by_id(db: Session, id: int) -> UserResponseDTO:
        user = UserRepository.get_by_id(db, id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponseDTO.model_validate(user)

    @staticmethod
    def get_user_by_username(db: Session, username: str) -> UserResponseDTO:
        user = UserRepository.get_by_username(db, username)
        if user is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return UserResponseDTO.model_validate(user)

    @staticmethod
    def update_user_avatar(user_id: int, dto: UserUpdateAvatarDto, db: Session):
        return UserRepository.update_avatar(user_id, dto.avatar_id, db)
    
    @staticmethod
    def get_all(db: Session) -> list[UserResponseDTO]:
        users = UserRepository.get_all(db)
        return [UserResponseDTO.model_validate(user) for user in users]

    @staticmethod
    def update_user_points(user_id: int, dto: UserUpdatePointsDto, db: Session):
        try:
            return UserRepository.update_points(user_id, dto.total_points, db)
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    @staticmethod
    def get_users_by_session(db: Session, session_id: int) -> list[UserResponseDTO]:
        users = UserRepository.get_users_by_session_attendance(db, session_id)
        return [UserResponseDTO.model_validate(user) for user in users]
