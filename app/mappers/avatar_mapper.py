from app.entities.avatar import Avatar

def create_avatar_entity(name: str, image_url: str, is_active: bool = True) -> Avatar:
    return Avatar(
        name=name,
        image_url=image_url,
        is_active=is_active
    )
