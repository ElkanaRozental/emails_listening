from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.postgres_database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    ip_address = Column(String(100), nullable=False)

    location = relationship("Location", back_populates="user", uselist=False)
    device = relationship("Device", back_populates="user", uselist=False)
    hostage_sentences = relationship("SentenceHostage", back_populates="user")
    explosive_sentences = relationship("SentenceExplosive", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email} ip_address={self.ip_address}, location={self.location}, device={self.device}, hostage_sentences={self.hostage_sentences}, explosive_sentence={self.explosive_sentences} >"