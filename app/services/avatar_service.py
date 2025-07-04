from sqlalchemy.orm import Session as DBSession
from app.repositories.avatar_repository import AvatarRepository
from app.dtos.avatar_dtos import AvatarResponseDTO
from app.dtos.avatar_dtos import AvatarCreateDTO
from app.mappers.avatar_mapper import create_avatar_entity

class AvatarService:

    @staticmethod
    def list_active_avatars(db: DBSession) -> list[AvatarResponseDTO]:
        avatars = AvatarRepository.list_active(db)
        return [AvatarResponseDTO.model_validate(a) for a in avatars]
    
    @staticmethod
    def create(db: DBSession, dto: AvatarCreateDTO) -> AvatarResponseDTO:
        avatar = create_avatar_entity(dto)
        db.add(avatar)
        db.commit()
        db.refresh(avatar)
        return AvatarResponseDTO.model_validate(avatar)
    

    @staticmethod
    def get_by_id(db: DBSession, avatar_id: int) -> AvatarResponseDTO:
        session = AvatarRepository.get_by_id(db, avatar_id)
        if not session:
            raise Exception("Session not found")
        return AvatarResponseDTO.model_validate(session)