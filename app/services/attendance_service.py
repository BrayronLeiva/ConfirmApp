from sqlalchemy.orm import Session as DBSession
from fastapi import HTTPException
from app.dtos.attendance_dtos import AttendanceCreateDTO, AttendanceResponseDTO
from app.mappers.attendance_mapper import attendance_create_dto_to_entity
from app.repositories.attendance_repository import AttendanceRepository

class AttendanceService:

    @staticmethod
    def register_attendance(db: DBSession, dto: AttendanceCreateDTO) -> AttendanceResponseDTO:
        try:
            attendance = attendance_create_dto_to_entity(dto)
            attendance = AttendanceRepository.create(db, attendance)
            return AttendanceResponseDTO.model_validate(attendance)
        except Exception:
            raise HTTPException(status_code=400, detail="Attendance already recorded or invalid")

    @staticmethod
    def list_attendance_by_user(db: DBSession, user_id: int) -> list[AttendanceResponseDTO]:
        records = AttendanceRepository.list_by_user(db, user_id)
        return [AttendanceResponseDTO.model_validate(r) for r in records]
