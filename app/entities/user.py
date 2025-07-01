from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship  
from datetime import datetime
from app.entities.user_role import UserRole
from datetime import datetime, timezone
from app.config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    total_points = Column(Integer, default=0)
    date_register = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    rol = Column(Enum(UserRole), default=UserRole.YOUNG)
    avatar_id = Column(Integer, ForeignKey("avatars.id"))
    avatar = relationship("Avatar")
