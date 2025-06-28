from sqlalchemy.orm import Session as DBSession
from app.entities.session import Session

class SessionRepository:

    @staticmethod
    def create(db: DBSession, session: Session) -> Session:
        db.add(session)
        db.commit()
        db.refresh(session)
        return session

    @staticmethod
    def list_all(db: DBSession) -> list[Session]:
        return db.query(Session).order_by(Session.level).all()

    @staticmethod
    def get_by_id(db: DBSession, session_id: int) -> Session | None:
        return db.query(Session).filter(Session.id == session_id).first()
