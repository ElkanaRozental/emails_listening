from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.db.postgres_database import Base


class Sentence(Base):
    __tablename__ = "sentences"
    id = Column(Integer,primary_key=True, autoincrement=True)
    sentence = Column(String(100), nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="sentences")