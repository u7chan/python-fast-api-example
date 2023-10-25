from abc import ABC, abstractmethod

from app.domain.entity.login import Login
from app.domain.entity.session import Session


class LoginUseCase(ABC):
    @abstractmethod
    def execute(self, login: Login) -> Session:
        raise NotImplementedError
