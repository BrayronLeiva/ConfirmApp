
from app.dtos.session_dtos import SessionCreateDTO, SessionResponseDTO
from app.services.session_service import SessionService
from fastapi import APIRouter, Depends, HTTPException
from app.config.database import SessionLocal
from sqlalchemy.orm import Session
from app.dtos.users import UserUpdatePointsDto 
router = APIRouter(prefix="/v1/sessions", tags=["sessions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=SessionResponseDTO)
def create_session(dto: SessionCreateDTO, db: Session = Depends(get_db)):
    return SessionService.create(db, dto)

@router.get("", response_model=list[SessionResponseDTO])
def list_sessions(db: Session = Depends(get_db)):
    return SessionService.list_all(db)

@router.get("/{session_id}", response_model=SessionResponseDTO)
def get_session(session_id: int, db: Session = Depends(get_db)):
    return SessionService.get_by_id(db, session_id)
