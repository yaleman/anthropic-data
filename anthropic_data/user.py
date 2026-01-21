from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field


class User(BaseModel):
    uuid: UUID
    full_name: str
    email_address: Optional[str] = Field(None)
    verified_phone_number: Optional[str] = Field(None)

    model_config = ConfigDict(extra="forbid")
