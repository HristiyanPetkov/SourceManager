from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db
import crud.organization as organization_crud
from schemas.organization import Organization

router = APIRouter(
    prefix="/login",
    tags=["login"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=Organization)
def index(db: Session = Depends(get_db)):
    return organization_crud.read_organization(1, db)
