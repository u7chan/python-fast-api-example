from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from random import randint
from hashlib import sha256

from app.domain.entity.session import Session


class SessionRepository(ABC):
    @abstractmethod
    def create(self, user_id: str) -> Session:
        raise NotImplementedError()


class SessionRepositoryInMemory(SessionRepository):
    # In-memory session storage (for temporary validation)
    tmp_session = {}

    def _debug_print(self):
        dump = {}
        for key, value in self.tmp_session.items():
            dump[key] = value.to_str()
        print("#session", dump)

    def create(self, user_id: str) -> Session:
        salt = str(len(self.tmp_session) + randint(0, 1000000))
        session_id = sha256(bytes(salt, "ascii")).hexdigest()
        expires = datetime.now() + timedelta(
            milliseconds=1 * 24 * 60 * 60  # expiry period of next days.
        )
        session = Session(id=session_id, expires=expires)
        self.tmp_session[user_id] = session
        self._debug_print()
        return session
