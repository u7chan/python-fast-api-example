from abc import ABC, abstractmethod
from random import randint
from hashlib import sha256


class SessionRepository(ABC):
    @abstractmethod
    def create(self, user_id: str) -> str:
        raise NotImplementedError()


class SessionRepositoryInMemory(SessionRepository):
    # In-memory session storage (for temporary validation)
    tmp_session = {}

    def create(self, user_id: str) -> str:
        salt = str(len(self.tmp_session) + randint(0, 1000000))
        session_id = sha256(bytes(salt, "ascii")).hexdigest()
        self.tmp_session[user_id] = session_id
        print("#salt", salt)
        print("#tmp_session", self.tmp_session)
        return session_id
