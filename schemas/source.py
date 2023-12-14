from wsgiref.validate import validator

from pydantic import BaseModel, field_validator
from enum import Enum
from ipaddress import IPv4Address, IPv4Network


class SourceType(Enum):
    ip = "ip"
    domain = "domain"
    ip_range = "ip_range"


class SourceCreate(BaseModel):
    id: int
    type: SourceType
    value: str
    organization_id: int


class Source(BaseModel):
    id: int

    type: SourceType
    value: str
    organization_id: int
