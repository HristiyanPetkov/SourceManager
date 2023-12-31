from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud.user as user_crud
from dependencies import get_db
from schemas.user import User, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[User])
def index(db: Session = Depends(get_db)):
    return user_crud.list_all(db)


@router.get("/{user_id}", response_model=User)
def show(user_id: int, db: Session = Depends(get_db)):
    return user_crud.read_user(user_id, db)


@router.post("/", response_model=User)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(user, db)


@router.put("/{user_id}", response_model=User)
def update(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return user_crud.update_user(user_id, user, db)


@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    return user_crud.delete_user(user_id, db)
