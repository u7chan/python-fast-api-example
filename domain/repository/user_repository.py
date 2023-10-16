from abc import ABC, abstractmethod

from domain.value_object import User
from sqlalchemy.orm.session import Session
from infrastructure.database.models import UserDto


class UserRepository(ABC):
    @abstractmethod
    def fetch_all(self) -> [User]:
        raise NotImplementedError


class UserRepositoryImpl(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def fetch_all(self) -> [User]:
        try:
            user_dtos = (
                self.session.query(UserDto)
                .order_by(UserDto.updated_at.desc())
                .limit(100)
                .all()
            )
        except:
            raise

        if len(user_dtos) == 0:
            return []

        return list(map(lambda dto: dto.to_entity(), user_dtos))
