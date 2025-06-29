from app.dtos.attendance_dtos import AttendanceCreateDTO
from app.entities.attendance import Attendance

def attendance_create_dto_to_entity(dto: AttendanceCreateDTO) -> Attendance:
    return Attendance(
        user_id=dto.user_id,
        session_id=dto.session_id
    )
