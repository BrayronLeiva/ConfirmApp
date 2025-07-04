from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.config.database import Base

class QuestionCategory(Base):
    __tablename__ = "question_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    game_type = Column(String, nullable=False)  # Ej: "MULTIPLE_CHOICE", "TRUE_FALSE"
    is_active = Column(Boolean, default=True)

    questions = relationship("GameQuestion", back_populates="category")
