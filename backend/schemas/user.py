from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    organization_id: int


class User(BaseModel):
    id: int

    name: str
    organization_id: int
