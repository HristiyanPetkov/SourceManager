from enum import Enum

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import source as source_model
from schemas import source as source_schema


class SourceType(Enum):
    ip = "ip"
    domain = "domain"
    ip_range = "ip_range"


def create_source(source: source_schema.SourceCreate, db: Session):
    db_source = source_model.Source(type=source.type.name, value=source.value, comment=source.comment, organization_id=source.organization_id, user_id=source.user_id)
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
    old_source.type = source.type.name
    old_source.value = source.value
    old_source.comment = source.comment
    old_source.organization_id = source.organization_id
    old_source.user_id = source.user_id
    db.commit()
    db.refresh(old_source)
    return old_source


def delete_source(source_id: int, db: Session):
    source = read_source(source_id, db)
    db.delete(source)
    db.commit()
    return {"message": "Source deleted successfully"}


def list_all(db: Session, skip: int = 0, limit: int = 100):
    return (db.query(source_model.Source)
            .offset(skip)
            .limit(limit)
            .all())


def read_source_by_type(type: SourceType, organization_id: int, db: Session):
    return (db.query(source_model.Source)
            .filter(source_model.Source.type == type,
                    source_model.Source.organization_id == organization_id)
            .all())
