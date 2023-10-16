from abc import ABC, abstractmethod

from domain.repository.user_repository import UserRepository
from domain.value_object import User


class CreateUserUseCase(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError


class CreateUserUseCaseImpl(CreateUserUseCase):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self) -> User:
        try:
            user = self.user_repository.save(
                User(name="una", email="una@example.com")  # TODO: fixed user
            )
        except:
            raise
        return user
