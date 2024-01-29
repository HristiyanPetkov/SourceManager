from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    comment: str
    phone: str
    organization_id: int


class UserResponse(BaseModel):
    id: int

    name: str
    email: str
    comment: str
    phone: str
    organization_id: int
    organization_name: str
