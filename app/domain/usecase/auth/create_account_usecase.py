from abc import ABC, abstractmethod


class CreateAccountCase(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError
