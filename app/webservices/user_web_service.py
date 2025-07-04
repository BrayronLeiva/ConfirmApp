from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.services.user_service import UserService
from app.dtos.users import UserCreateDTO, UserResponseDTO, AuthRequestDTO, AuthResponseDTO, UserUpdateAvatarDto
from typing import Optional, Union, List
from app.dtos.users import UserUpdatePointsDto 

router = APIRouter(prefix="/v1/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=UserResponseDTO)
def register_user(dto: UserCreateDTO, db: Session = Depends(get_db)):
    return UserService.register(db, dto)

@router.post("/login", response_model=AuthResponseDTO)
def login(dto: AuthRequestDTO, db: Session = Depends(get_db)):
    return UserService.login(db, dto)

@router.get("", response_model=Union[UserResponseDTO, List[UserResponseDTO]])
def get_users(
    username: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    if username:
        return UserService.get_user_by_username(db, username)
    return UserService.get_all(db)


@router.get("/{user_id}", response_model=UserResponseDTO)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return UserService.get_user_by_id(db, user_id)



@router.patch("/{user_id}/avatar")
def update_user_avatar(
    user_id: int,
    dto: UserUpdateAvatarDto,
    db: Session = Depends(get_db)
):
    return UserService.update_user_avatar(user_id, dto, db)

@router.patch("/{user_id}/points")
def update_user_points(
    user_id: int,
    dto: UserUpdatePointsDto,
    db: Session = Depends(get_db)
):
    return UserService.update_user_points(user_id, dto, db)

@router.get("/by-session/{session_id}", response_model=List[UserResponseDTO])
def get_users_by_session(session_id: int, db: Session = Depends(get_db)):
    return UserService.get_users_by_session(db, session_id)
