from pydantic import BaseModel, constr


class OrganizationCreate(BaseModel):
    name: constr(min_length=1, max_length=100)


class Organization(BaseModel):
    id: int
    name: str
