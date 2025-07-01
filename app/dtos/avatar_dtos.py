from pydantic import BaseModel, HttpUrl, ConfigDict

class AvatarResponseDTO(BaseModel):
    id: int
    name: str
    image_url: HttpUrl
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

class AvatarCreateDTO(BaseModel):
    name: str
    image_url: HttpUrl

    model_config = ConfigDict(from_attributes=True)