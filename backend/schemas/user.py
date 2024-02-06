from pydantic import BaseModel, EmailStr, constr, field_validator


class UserCreate(BaseModel):
    name: constr(min_length=1, max_length=100)
    email: EmailStr
    password: constr(min_length=8)
    comment: constr(max_length=255)
    phone: constr(min_length=10, max_length=10)
    organization_id: int

    @field_validator("phone")
    def validate_phone(cls, value):
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits")
        return value

    @field_validator("password")
    def validate_password_strength(cls, value):
        if not any(char.isupper() for char in value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit")
        return value


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
    phone: str
    organization_id: int
    organization_name: str
