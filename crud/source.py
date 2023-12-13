from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import source as source_model
from schemas import source as source_schema


def create_source(source: source_schema.SourceCreate, db: Session):
    db_source = source_model.Source(type=source.type, value=source.value, organization_id=source.organization_id)
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
    old_source.type = source.type
    old_source.value = source.value
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
