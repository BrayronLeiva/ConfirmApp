from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.services.avatar_service import AvatarService
from app.dtos.avatar_dtos import AvatarResponseDTO

router = APIRouter(prefix="/avatars", tags=["avatars"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("", response_model=list[AvatarResponseDTO])
def list_avatars(db: Session = Depends(get_db)):
    return AvatarService.list_active_avatars(db)
