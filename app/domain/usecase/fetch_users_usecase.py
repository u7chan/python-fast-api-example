from abc import ABC, abstractmethod

from app.domain.repository.user_repository import UserRepository
from app.domain.entity import User


class FetchUsersUseCase(ABC):
    @abstractmethod
    def execute(self) -> [User]:
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
