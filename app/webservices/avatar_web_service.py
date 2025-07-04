from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.services.avatar_service import AvatarService
from app.dtos.avatar_dtos import AvatarResponseDTO, AvatarCreateDTO

router = APIRouter(prefix="/v1/avatars", tags=["avatars"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("", response_model=list[AvatarResponseDTO])
def list_avatars(db: Session = Depends(get_db)):
    return AvatarService.list_active_avatars(db)


@router.post("/create", response_model=AvatarResponseDTO)
def create_avatar(dto: AvatarCreateDTO, db: Session = Depends(get_db)):
    return AvatarService.create(db, dto)


@router.get("/{avatar_id}", response_model=AvatarResponseDTO)
def get_session(avatar_id: int, db: Session = Depends(get_db)):
    return AvatarService.get_by_id(db, avatar_id)
