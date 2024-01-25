from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship


class Organization(Base):
    __tablename__ = 'organizations'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    user = relationship("User", back_populates="organization", cascade="all, delete-orphan")
    source = relationship("Source", back_populates="organization", cascade="all, delete-orphan")
