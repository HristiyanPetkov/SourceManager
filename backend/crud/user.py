import bcrypt
import base64
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import user as user_model, organization as organization_model
from crud.organization import get_organization_name, get_organization_by_name, create_organization
from schemas import user as user_schema
from schemas import organization as organization_schema


def create_user(user: user_schema.UserCreate, db: Session):
    organization = get_organization_by_name(db, user.organization)
    if not organization:
        organization = create_organization(organization_schema.OrganizationCreate(name=user.organization), db)

    db_user = user_model.User(
        name=user.name,
        email=user.email,
        comment=user.comment,
        organization_id=organization.id,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return get_user_response(db_user, db)


def read_raw_user(user_id: int, db: Session):
    user = (db.query(user_model.User)
            .filter(user_model.User.id == user_id)
            .first())

    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


def read_user(user_id: int, db: Session):
    user = read_raw_user(user_id, db)
    return get_user_response(user, db)


def update_user(user_id: int, user: user_schema.UserCreate, db: Session):
    old_user = read_raw_user(user_id, db)
    old_user.name = user.name
    old_user.email = user.email
    old_user.comment = user.comment
    old_user.organization_id = user.organization_id
    db.commit()
    db.refresh(old_user)

    return get_user_response(old_user, db)


def delete_user(user_id: int, db: Session):
    user = read_raw_user(user_id, db)

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}


def list_all(db: Session, skip: int = 0, limit: int = 100):
    users = (db.query(user_model.User)
             .offset(skip)
             .limit(limit)
             .all())

    return [get_user_response(user, db) for user in users if isinstance(user, user_model.User)]


def get_user_response(user: user_model.User, db: Session) -> user_schema.UserResponse:
    organization_name = get_organization_name(db, user.organization_id)

    return user_schema.UserResponse(**user.__dict__, organization_name=organization_name)


def authenticate(user: user_schema.UserLogin, db: Session):
    db_user = (db.query(user_model.User)
               .filter(user_model.User.email == user.email)
               .first())

    if bcrypt.checkpw(user.password.encode('utf-8'), base64.b64decode(db_user.password.encode('utf-8'))):
        return get_user_response(db_user, db)
    raise HTTPException(
        status_code=401,
        detail="Incorrect email or password",
        headers={"WWW-Authenticate": "Bearer"},
    )


def read_user_by_email(user_email: str, db: Session):
    user = (db.query(user_model.User)
            .filter(user_model.User.email == user_email)
            .first())

    if user:
        return get_user_response(user, db)
    else :
        create_user(user_schema.UserCreate(
            name=user_email,
            email=user_email,
            comment="",
            organization_id=1,
        ), db)
