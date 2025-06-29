from sqlalchemy import Column, String, Integer, DateTime, Text
from datetime import datetime, timezone
from app.config.database import Base

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    summary = Column(Text, nullable=True)
    scheduled_at = Column(DateTime, nullable=False)
    level = Column(Integer, nullable=False)
    qr_code = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
