from datetime import datetime


class Session:
    def __init__(self, id: str, expires: datetime):
        self.id = id
        self.expires = expires

    def to_str(self) -> str:
        return f"{self.id}: {self.expires}"
