from sqlalchemy.orm import Session as DBSession
from app.dtos.session_dtos import SessionCreateDTO, SessionResponseDTO
from app.mappers.session_mapper import session_create_dto_to_entity
from app.repositories.session_repository import SessionRepository

class SessionService:

    @staticmethod
    def create(db: DBSession, dto: SessionCreateDTO) -> SessionResponseDTO:
        session = session_create_dto_to_entity(dto)
        session = SessionRepository.create(db, session)
        return SessionResponseDTO.model_validate(session)

    @staticmethod
    def list_all(db: DBSession) -> list[SessionResponseDTO]:
        sessions = SessionRepository.list_all(db)
        return [SessionResponseDTO.model_validate(s) for s in sessions]

    @staticmethod
    def get_by_id(db: DBSession, session_id: int) -> SessionResponseDTO:
        session = SessionRepository.get_by_id(db, session_id)
        if not session:
            raise Exception("Session not found")
        return SessionResponseDTO.model_validate(session)
