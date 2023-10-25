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
