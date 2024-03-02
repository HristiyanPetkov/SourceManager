from pydantic import BaseModel, constr, field_validator
from enum import Enum


class SourceType(str, Enum):
    ip = "ip"
    domain = "domain"
    ip_range = "ip_range"


class SourceCreate(BaseModel):
    type: SourceType
    value: constr(min_length=1)
    comment: constr(max_length=255)
    organization_id: int
    user_id: int

    @field_validator("type")
    def validate_type(cls, value):
        if value not in SourceType:
            raise ValueError("Invalid source type")
        return value


class Source(BaseModel):
    id: int

    type: SourceType
    value: str
    comment: str
    organization_id: int
    user_id: int
