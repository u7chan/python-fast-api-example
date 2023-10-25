from abc import ABC, abstractmethod

from app.domain.entity.create_account import CreateAccount


class CreateAccountCase(ABC):
    @abstractmethod
    def execute(self, create_account: CreateAccount):
        raise NotImplementedError
