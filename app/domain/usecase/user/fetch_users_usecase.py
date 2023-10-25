from abc import ABC, abstractmethod

from app.domain.entity.user import User


class FetchUsersUseCase(ABC):
    @abstractmethod
    def execute(self) -> [User]:
        raise NotImplementedError
