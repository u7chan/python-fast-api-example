from typing import Optional
from uuid import uuid4


class User:
    def __init__(
        self,
        name: str,
        email: str,
        id: Optional[str] = None,
        updated_at: Optional[str] = None,
    ):
        self.id = id
        self.name = name
        self.email = email
        self.updated_at = updated_at

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, User):
            return self.id == obj.id

    def set_new_id(self):
        self.id = str(uuid4())
