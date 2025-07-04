from sqlalchemy.orm import Session, joinedload
from app.entities.user import User
from app.entities.avatar import Avatar
from app.entities.attendance import Attendance

class UserRepository:

    @staticmethod
    def get_by_username(db: Session, username: str) -> User | None:
        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def create(db: Session, user: User) -> User:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_by_id(db: Session, id: int) -> User | None:
        return db.query(User).options(joinedload(User.avatar)).filter(User.id == id).first()
    
    @staticmethod
    def get_by_username(db: Session, username: str) -> User | None:
        return db.query(User).options(joinedload(User.avatar)).filter(User.username == username).first()

    @staticmethod
    def update_avatar(user_id: int, avatar_id: int, db: Session) -> User:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError("User not found")

        avatar = db.query(Avatar).filter(Avatar.id == avatar_id, Avatar.is_active == True).first()
        if not avatar:
            raise ValueError("Avatar not found or inactive")

        user.avatar_id = avatar_id
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_all(db: Session) -> list[User]:
        return db.query(User).order_by(User.id).all()
    
    @staticmethod
    def update_points(user_id: int, new_points: int, db: Session) -> User:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError("User not found")

        user.total_points = new_points
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def get_users_by_session_attendance(db: Session, session_id: int) -> list[User]:
        return (
            db.query(User)
            .join(Attendance, User.id == Attendance.user_id)
            .filter(Attendance.session_id == session_id)
            .all()
        )
