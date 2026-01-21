from uuid import UUID
from pathlib import Path
from typing import Optional

from pydantic import RootModel, BaseModel, ConfigDict

from .loader import Loader
from .user import User
from .users import Users


class Memory(BaseModel):
    account_uuid: UUID

    conversations_memory: str
    model_config = ConfigDict(
        extra="forbid",
    )

    def try_find_user(self, filename: str | Path) -> Optional[User]:
        """see if we can find the user in the users data file"""
        users = Users.load(filename)

        found_users = [user for user in users.root if user.uuid == self.account_uuid]
        if found_users:
            return found_users[0]
        return None


class Memories(RootModel[list[Memory]], Loader):
    root: list[Memory]


if __name__ == "__main__":
    memories = Memories.load("memories.json")
    print(memories.model_dump_json(indent=4))
