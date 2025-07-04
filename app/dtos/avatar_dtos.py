from pydantic import BaseModel, ConfigDict

class AvatarResponseDTO(BaseModel):
    id: int
    name: str
    image_url: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

class AvatarCreateDTO(BaseModel):
    name: str
    image_url: str

    model_config = ConfigDict(from_attributes=True)