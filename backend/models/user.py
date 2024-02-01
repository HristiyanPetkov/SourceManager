from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    comment = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    organization_id = Column(Integer, ForeignKey('organizations.id'))

    organization = relationship("Organization", back_populates="user")
