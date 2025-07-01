from sqlalchemy import Column, Integer, String, Boolean
from datetime import datetime, timezone
from app.config.database import Base

class Avatar(Base):
    __tablename__ = "avatars"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    image_url = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, default=True)
