from abc import ABC, abstractmethod

from app.domain.repository.user_repository import UserRepository
from app.domain.entity import User


class CreateUserUseCase(ABC):
    @abstractmethod
    def execute(self, user: User) -> User:
        raise NotImplementedError


class CreateUserUseCaseImpl(CreateUserUseCase):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, data: User) -> User:
        try:
            user = self.user_repository.save(data)
        except:
            raise
        return user
