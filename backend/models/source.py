import logging
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, event
from database import Base
from sqlalchemy.orm import relationship
from enum import Enum

logging.basicConfig(filename='log_file.log', level=logging.INFO)
logger = logging.getLogger(__name__)


class SourceType(Enum):
    ip = "ip"
    domain = "domain"
    ip_range = "ip_range"


class Source(Base):
    __tablename__ = 'sources'
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50), index=True)
    value = Column(String(50), index=True)
    comment = Column(String(50), nullable=False)
    organization_id = Column(Integer, ForeignKey('organizations.id'))

    organization = relationship("Organization", back_populates="source")


@event.listens_for(Source, 'before_insert')
def before_insert_listener(mapper, connection, target):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f"{timestamp} - Inserting a new Source record: ID={target.id}, Type={target.type}, Value={target.value}, Comment={target.comment}, OrganizationID={target.organization_id}")


@event.listens_for(Source, 'before_update')
def before_update_listener(mapper, connection, target):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    changes = {attr.key: getattr(target, attr.key, None) for attr in target.__table__.columns}
    logger.info(f"{timestamp} - Updating Source record: ID={target.id}, Changes={changes}, OrganizationID={target.organization_id}")


@event.listens_for(Source, 'before_delete')
def before_delete_listener(mapper, connection, target):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f"{timestamp} - Deleting Source record: ID={target.id}, Type={target.type}, Value={target.value}, Comment={target.comment}, OrganizationID={target.organization_id}")
