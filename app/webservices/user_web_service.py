from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.services.user_service import UserService
from app.dtos.users import UserCreateDTO, UserResponseDTO, AuthRequestDTO, AuthResponseDTO

router = APIRouter(prefix="/v1/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserResponseDTO)
def register_user(dto: UserCreateDTO, db: Session = Depends(get_db)):
    return UserService.register(db, dto)

@router.post("/login", response_model=AuthResponseDTO)
def login(dto: AuthRequestDTO, db: Session = Depends(get_db)):
    return UserService.login(db, dto)

@router.get("/{user_id}", response_model=UserResponseDTO)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return UserService.get_user_by_id(db, user_id)
