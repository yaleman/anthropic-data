from typing import Self
from pathlib import Path


class Loader:
    @classmethod
    def load(cls, filename: Path | str) -> Self:
        if isinstance(filename, str):
            filename = Path(filename)
        if hasattr(cls, "model_validate_json"):
            res: Self = getattr(cls, "model_validate_json")(filename.read_text())
            return res
        raise TypeError("Loader can only be used with Pydantic BaseModel subclasses.")
