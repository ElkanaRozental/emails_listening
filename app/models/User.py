from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.postgres_database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    ip_address = Column(String(100), nullable=False)

    location = relationship("Location", back_populates="user", uselist=False)
    device = relationship("Device", back_populates="user", uselist=False)
    sentences = relationship("Sentence", back_populates="user")