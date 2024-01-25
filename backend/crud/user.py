from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import user as user_model
from schemas import user as user_schema


def create_user(user: user_schema.UserCreate, db: Session):
    db_user = user_model.User(name=user.name, email=user.email, comment=user.comment, phone=user.phone,
                              organization_id=user.organization_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def read_user(user_id: int, db: Session):
    user = (db.query(user_model.User)
            .filter(user_model.User.id == user_id)
            .first())
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


def update_user(user_id: int, user: user_schema.UserCreate, db: Session):
    old_user = read_user(user_id, db)
    if not old_user:
        raise HTTPException(status_code=404, detail="User not found")
    old_user.name = user.name
    old_user.email = user.email
    old_user.comment = user.comment
    old_user.phone = user.phone
    old_user.organization_id = user.organization_id
    db.commit()
    db.refresh(old_user)
    return old_user


def delete_user(user_id: int, db: Session):
    user = read_user(user_id, db)
    if user:
        db.delete(user)
        db.commit()
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")


def list_all(db: Session, skip: int = 0, limit: int = 100):
    return (db.query(user_model.User)
            .offset(skip)
            .limit(limit)
            .all())
