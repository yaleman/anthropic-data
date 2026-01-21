from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, RootModel, ConfigDict, Field

from .loader import Loader
from .user import User


class Doc(BaseModel):
    uuid: UUID
    filename: str
    content: str
    created_at: datetime
    updated_at: Optional[datetime] = Field(None)

    model_config = ConfigDict(extra="forbid")


class Project(BaseModel):
    creator: User
    name: str
    uuid: UUID
    created_at: datetime
    updated_at: datetime
    docs: list[Doc] = Field(default_factory=list)
    is_private: bool
    is_starter_project: bool
    description: str
    prompt_template: str
    model_config = ConfigDict(extra="forbid")


class Projects(RootModel[list[Project]], Loader):
    pass


if __name__ == "__main__":
    projects = Projects.load("projects.json")
    print(projects)
