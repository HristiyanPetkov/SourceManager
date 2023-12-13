from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud.organization as organization_crud
from dependencies import get_db
from schemas.organization import Organization, OrganizationCreate

router = APIRouter(
    prefix="/organizations",
    tags=["organizations"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[Organization])
def index(db: Session = Depends(get_db)):
    return organization_crud.list_all(db)


@router.get("/{organization_id}", response_model=Organization)
def show(organization_id: int, db: Session = Depends(get_db)):
    return organization_crud.read_organization(organization_id, db)


@router.post("/", response_model=Organization)
def create(organization: OrganizationCreate, db: Session = Depends(get_db)):
    return organization_crud.create_organization(organization, db)


@router.put("/{organization_id}", response_model=Organization)
def update(organization_id: int, organization: OrganizationCreate, db: Session = Depends(get_db)):
    return organization_crud.update_organization(organization_id, organization, db)


@router.delete("/{organization_id}")
def delete(organization_id: int, db: Session = Depends(get_db)):
    return organization_crud.delete_organization(organization_id, db)
