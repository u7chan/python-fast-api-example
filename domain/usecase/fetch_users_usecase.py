from abc import ABC, abstractmethod

from domain.repository.user_repository import UserRepository
from domain.value_object import User


class FetchUsersUseCase(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError


class FetchUsersUseCaseImpl(FetchUsersUseCase):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self) -> [User]:
        try:
            users = self.user_repository.fetch_all()
        except:
            raise
        return users
