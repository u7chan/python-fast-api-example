from typing import Optional


class CreateAccount:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password
