
from sqlalchemy.orm import Session as DBSession
from app.entities.session import Session
from app.entities.attendance import Attendance

class AttendanceRepository:

    @staticmethod
    def create(db: Session, attendance: Attendance) -> Attendance:
        db.add(attendance)
        db.commit()
        db.refresh(attendance)
        return attendance

    @staticmethod
    def list_by_user(db: Session, user_id: int) -> list[Attendance]:
        return db.query(Attendance).filter(Attendance.user_id == user_id).all()
