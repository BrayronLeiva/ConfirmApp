from app.dtos.session_dtos import SessionCreateDTO
from app.entities.session import Session

def session_create_dto_to_entity(dto: SessionCreateDTO) -> Session:
    return Session(
        name=dto.name,
        summary=dto.summary,
        scheduled_at=dto.scheduled_at,
        level=dto.level,
        qr_code=dto.qr_code
    )
