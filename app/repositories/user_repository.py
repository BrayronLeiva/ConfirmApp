from sqlalchemy.orm import Session, joinedload
from app.entities.user import User

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
