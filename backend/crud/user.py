from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import user as user_model, organization as organization_model
from schemas import user as user_schema


def create_user(user: user_schema.UserCreate, db: Session):
    db_user = user_model.User(name=user.name, email=user.email, comment=user.comment, phone=user.phone,
                              organization_id=user.organization_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return get_user_response(db_user, db)

def read_user(user_id: int, db: Session):
    user = (db.query(user_model.User)
            .filter(user_model.User.id == user_id)
            .first())

    if user:
        return get_user_response(user, db)
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

    old_user.organization_name = (db.query(organization_model.Organization)
                           .filter(organization_model.Organization.id == old_user.organization_id)
                           .first()).name

    return old_user


def delete_user(user_id: int, db: Session):
    user = read_user(user_id, db)
    if user:
        db.delete(user)
        db.commit()
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")


def list_all(db: Session, skip: int = 0, limit: int = 100):
    users = (db.query(user_model.User)
             .offset(skip)
             .limit(limit)
             .all())

    return [get_user_response(user, db) for user in users if isinstance(user, user_model.User)]


def get_user_response(user: user_model.User, db: Session) -> user_schema.UserResponse:
    organization_name = (db.query(organization_model.Organization)
                         .filter(organization_model.Organization.id == user.organization_id)
                         .first()).name

    return user_schema.UserResponse(**user.__dict__, organization_name=organization_name)
