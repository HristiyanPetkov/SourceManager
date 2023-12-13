from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship


class Organization(Base):
    __tablename__ = 'organization'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    mail = Column(String(50), nullable=False)

    users = relationship("User", back_populates="organization")
