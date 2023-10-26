from abc import ABC, abstractmethod

from app.domain.entity.user import User


class UserRepository(ABC):
    @abstractmethod
    def fetch_all(self) -> [User]:
        raise NotImplementedError

    @abstractmethod
    def insert(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def update(self, user: User) -> User:
        raise NotImplementedError
