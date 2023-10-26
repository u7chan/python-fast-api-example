from typing import Optional
from datetime import datetime


class User:
    def __init__(
        self,
        name: str,
        email: str,
        id: Optional[str] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.name = name
        self.email = email
        self.updated_at = updated_at

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, User):
            return self.__dict__ == obj.__dict__
        raise NotImplementedError
