from uuid import UUID
from pydantic import BaseModel, ConfigDict
from .loader import Loader


class Account(BaseModel, Loader):
    uuid: UUID

    model_config = ConfigDict(extra="forbid")
