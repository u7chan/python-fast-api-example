from abc import ABC, abstractmethod

from app.domain.entity.user import User


class UserRepository(ABC):
    @abstractmethod
    def fetch_all(self) -> [User]:
        raise NotImplementedError

    @abstractmethod
    def save(self, user: User) -> User:
        raise NotImplementedError
