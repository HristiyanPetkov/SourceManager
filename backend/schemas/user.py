from pydantic import BaseModel, EmailStr, constr, field_validator


class UserCreate(BaseModel):
    name: str
    email: str
    comment: str
    organization: str


class UserLogin(BaseModel):
    email: EmailStr
    password: constr(min_length=8)

    @field_validator("password")
    def validate_password_strength(cls, value):
        if not any(char.isupper() for char in value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit")
        return value


class UserResponse(BaseModel):
    id: int

    name: str
    email: str
    comment: str
    organization_id: int
    organization_name: str
