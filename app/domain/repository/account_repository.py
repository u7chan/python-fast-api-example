from abc import ABC, abstractmethod

from app.domain.entity.account import Account


class AccountRepository(ABC):
    @abstractmethod
    def insert(self, account: Account) -> Account:
        raise NotImplementedError
