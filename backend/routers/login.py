from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db
import crud.user as user_crud
from schemas.user import UserLogin, UserResponse

router = APIRouter(
    prefix="/login",
    tags=["login"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=UserResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    return user_crud.login(user, db)

