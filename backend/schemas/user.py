from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    comment: str
    phone: str
    organization_id: int


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int

    name: str
    email: str
    comment: str
    phone: str
    organization_id: int
    organization_name: str
