from pydantic import BaseModel


class OrganizationCreate(BaseModel):
    name: str


class Organization(BaseModel):
    id: int
    name: str
