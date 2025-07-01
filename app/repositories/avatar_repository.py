from sqlalchemy.orm import Session
from app.entities.avatar import Avatar

class AvatarRepository:

    @staticmethod
    def list_active(db: Session) -> list[Avatar]:
        return db.query(Avatar).filter(Avatar.is_active == True).all()
