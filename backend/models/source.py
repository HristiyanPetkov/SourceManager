from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship
from enum import Enum


class SourceType(Enum):
    ip = "ip"
    domain = "domain"
    ip_range = "ip_range"


class Source(Base):
    __tablename__ = 'sources'
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    value = Column(String(50), index=True)
    organization_id = Column(Integer, ForeignKey('organizations.id'))

    organization = relationship("Organization", back_populates="source")
