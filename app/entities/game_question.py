
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship


class GameQuestion(Base):
    __tablename__ = "game_questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, nullable=False)
    option_a = Column(String, nullable=True)
    option_b = Column(String, nullable=True)
    option_c = Column(String, nullable=True)
    option_d = Column(String, nullable=True)
    correct_answer = Column(String, nullable=False)

    category_id = Column(Integer, ForeignKey("question_categories.id"), nullable=False)
    category = relationship("QuestionCategory", back_populates="questions")