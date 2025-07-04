from app.entities.avatar import Avatar
from app.dtos.avatar_dtos import AvatarCreateDTO

def create_avatar_entity(dto: AvatarCreateDTO) -> Avatar:
    return Avatar(
        name= dto.name,
        image_url=dto.image_url,
        is_active=True
    )
