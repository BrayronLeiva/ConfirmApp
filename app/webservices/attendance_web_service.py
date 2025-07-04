from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.dtos.attendance_dtos import AttendanceCreateDTO, AttendanceResponseDTO
from app.services.attendance_service import AttendanceService

router = APIRouter(prefix="/v1/attendances", tags=["attendances"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=AttendanceResponseDTO)
def register_attendance(dto: AttendanceCreateDTO, db: Session = Depends(get_db)):
    return AttendanceService.register_attendance(db, dto)

@router.get("/user/{user_id}", response_model=list[AttendanceResponseDTO])
def list_user_attendance(user_id: int, db: Session = Depends(get_db)):
    return AttendanceService.list_attendance_by_user(db, user_id)
