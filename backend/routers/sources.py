from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud.source as source_crud
from dependencies import get_db
from schemas.source import Source, SourceCreate, SourceType

router = APIRouter(
    prefix="/sources",
    tags=["sources"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[Source])
def index(db: Session = Depends(get_db)):
    return source_crud.list_all(db)


@router.get("/{source_id}", response_model=Source)
def show(source_id: int, db: Session = Depends(get_db)):
    return source_crud.read_source(source_id, db)


@router.get("/{type}/{organization_id}", response_model=list[Source])
def show(type: str, organization_id: int, db: Session = Depends(get_db)):
    return source_crud.read_source_by_type(SourceType(type), organization_id, db)


@router.post("/", response_model=Source)
def create(source: SourceCreate, db: Session = Depends(get_db)):
    return source_crud.create_source(source, db)


@router.put("/{source_id}", response_model=Source)
def update(source_id: int, source: SourceCreate, db: Session = Depends(get_db)):
    return source_crud.update_source(source_id, source, db)


@router.delete("/{source_id}")
def delete(source_id: int, db: Session = Depends(get_db)):
    return source_crud.delete_source(source_id, db)
