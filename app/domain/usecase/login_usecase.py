from abc import ABC, abstractmethod

from app.domain.entity.login import Login


class LoginUseCase(ABC):
    @abstractmethod
    def execute(self, login: Login) -> str:
        raise NotImplementedError
