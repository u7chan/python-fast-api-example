from abc import ABC, abstractmethod

from domain.value_object import User
from sqlalchemy.orm.session import Session
from infrastructure.database import UserDto
from infrastructure.database.models import UserEntity


class UserRepository(ABC):
    @abstractmethod
    def fetch_all(self) -> [User]:
        raise NotImplementedError


class UserRepositoryImpl(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def fetch_all(self) -> [User]:
        try:
            entities = (
                self.session.query(UserEntity)
                .order_by(UserEntity.updated_at.desc())
                .limit(100)
                .all()
            )
        except:
            raise

        if len(entities) <= 0:
            return []

        return list(map(lambda entity: UserDto.from_entity(entity), entities))
