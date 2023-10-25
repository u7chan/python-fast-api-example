from abc import ABC, abstractmethod

from app.domain.entity.user import User


class CreateUserUseCase(ABC):
    @abstractmethod
    def execute(self, user: User) -> User:
        raise NotImplementedError
