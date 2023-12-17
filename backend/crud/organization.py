from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import organization as organization_model
from schemas import organization as organization_schema


def create_organization(organization: organization_schema.OrganizationCreate, db: Session):
    db_organization = organization_model.Organization(name=organization.name, mail=organization.mail)
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization


def read_organization(organization_id: int, db: Session):
    organization = (db.query(organization_model.Organization)
                    .filter(organization_model.Organization.id == organization_id)
                    .first())
    if organization:
        return organization
    raise HTTPException(status_code=404, detail="Organization not found")


def update_organization(organization_id: int, organization: organization_schema.OrganizationCreate, db: Session):
    old_organization = read_organization(organization_id, db)
    if not old_organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    old_organization.name = organization.name
    old_organization.email = organization.email
    db.commit()
    db.refresh(old_organization)
    return old_organization


def delete_organization(organization_id: int, db: Session):
    organization = read_organization(organization_id, db)
    if organization:
        db.delete(organization)
        db.commit()
        return {"message": "Organization deleted successfully"}
    raise HTTPException(status_code=404, detail="Organization not found")


def list_all(db: Session, skip: int = 0, limit: int = 100):
    return (db.query(organization_model.Organization)
            .offset(skip)
            .limit(limit)
            .all())
