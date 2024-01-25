from enum import Enum
# from ipaddress import IPv4Address, IPv4Network

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import source as source_model
from schemas import source as source_schema


class SourceType(Enum):
    ip = "ip"
    domain = "domain"
    ip_range = "ip_range"


def create_source(source: source_schema.SourceCreate, db: Session):
    '''
    try:
        ip = IPv4Address(source.value)
        source.type = SourceType.ip
    except ValueError:
        pass
    try:
        ip_range = IPv4Network(source.value)
        source.type = SourceType.ip_range
    except ValueError:
        pass
    try:
        domain = source.value
        source.type = SourceType.domain
    except ValueError:
        pass
    '''
    db_source = source_model.Source(type=source.type.name, value=source.value, comment=source.comment, organization_id=source.organization_id)
    db.add(db_source)
    db.commit()
    db.refresh(db_source)
    return db_source


def read_source(source_id: int, db: Session):
    source = (db.query(source_model.Source)
              .filter(source_model.Source.id == source_id)
              .first())
    if source:
        return source
    raise HTTPException(status_code=404, detail="Source not found")


def update_source(source_id: int, source: source_schema.SourceCreate, db: Session):
    old_source = read_source(source_id, db)
    if not old_source:
        raise HTTPException(status_code=404, detail="Source not found")
    old_source.type = source.type.name
    old_source.value = source.value
    old_source.comment = source.comment
    old_source.organization_id = source.organization_id
    db.commit()
    db.refresh(old_source)
    return old_source


def delete_source(source_id: int, db: Session):
    source = read_source(source_id, db)
    if source:
        db.delete(source)
        db.commit()
        return {"message": "Source deleted successfully"}
    raise HTTPException(status_code=404, detail="Source not found")


def list_all(db: Session, skip: int = 0, limit: int = 100):
    return (db.query(source_model.Source)
            .offset(skip)
            .limit(limit)
            .all())


def read_source_ip_hosts(db):
    return (db.query(source_model.Source)
            .filter(source_model.Source.type == SourceType.ip.name)
            .all())


def read_source_ip_range_hosts(db):
    return (db.query(source_model.Source)
            .filter(source_model.Source.type == SourceType.ip_range.name)
            .all())


def read_source_domain_hosts(db):
    return (db.query(source_model.Source)
            .filter(source_model.Source.type == SourceType.domain.name)
            .all())
