from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.services.user_service import UserService
from app.dtos.users import UserCreateDTO, UserResponseDTO

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserResponseDTO)
def register_user(dto: UserCreateDTO, db: Session = Depends(get_db)):
    return UserService.register(db, dto)

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    token = UserService.login(db, email, password)
    return {"access_token": token, "token_type": "bearer"}

