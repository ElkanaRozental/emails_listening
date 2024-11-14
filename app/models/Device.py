from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.postgres_database import Base


class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer,primary_key=True, autoincrement=True)
    browser = Column(String(500), nullable=False)
    os = Column(String(100), nullable=False)
    device_id = Column(String(500), nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="device", uselist=False)