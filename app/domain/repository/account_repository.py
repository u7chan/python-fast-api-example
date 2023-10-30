from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entity.account import Account


class AccountRepository(ABC):
    @abstractmethod
    def insert(self, account: Account) -> Account:
        raise NotImplementedError

    @abstractmethod
    def find_by_login_id(self, login_id) -> Optional[Account]:
        raise NotImplementedError
