from pydantic import BaseModel, constr
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


class Source(BaseModel):
    id: int

    type: SourceType
    value: str
    comment: str
    organization_id: int
