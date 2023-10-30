from typing import Optional


class Account:
    def __init__(
        self,
        user_id: str,
        login_id: str,
        password: Optional[str] = None,
    ):
        self.user_id = user_id
        self.login_id = login_id
        self.password = password

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Account):
            return self.__dict__ == obj.__dict__
        raise NotImplementedError
