from pydantic import BaseModel


class OrganizationCreate(BaseModel):
    name: str
    mail: str
    user: int


class Organization(BaseModel):
    id: int
    name: str
    mail: str
