from pydantic import RootModel

from .loader import Loader
from .user import User


class Users(RootModel[list[User]], Loader):
    pass


if __name__ == "__main__":
    users = Users.load("users.json")
    print(users.model_dump_json(indent=4))
