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

    @field_validator("value")
    def validate_value(self, value):
        try:
            ip = IPv4Address(value)
            self.type = SourceType.ip
        except ValueError:
            pass
        try:
            ip_range = IPv4Network(value)
            self.type = SourceType.ip_range
        except ValueError:
            pass

        # TODO: Validate domain

        raise ValueError("Invalid value type")


class Source(BaseModel):
    id: int

    type: SourceType
    value: str
    organization_id: int
