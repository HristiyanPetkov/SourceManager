from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    comment: str
    phone: str
    organization_id: int


class User(BaseModel):
    id: int

    name: str
    email: str
    comment: str
    phone: str
    organization_id: int
