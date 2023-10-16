from abc import ABC, abstractmethod
from uuid import uuid4

from domain.value_object import User
from sqlalchemy.orm.session import Session
from infrastructure.database.models import UserDto


class UserRepository(ABC):
    @abstractmethod
    def fetch_all(self) -> [User]:
        raise NotImplementedError

    @abstractmethod
    def save(self, user: User) -> User:
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

    def save(self, user: User) -> User:
        try:
            if user.id is None:
                user_dto = UserDto.from_entity(user)
                user_dto.id = str(uuid4())
                self.session.add(user_dto)
            else:
                user_dto = UserDto.from_entity(user)
                _user = self.session.query(UserDto).filter_by(id=user.id).one()
                _user.update_from_dto(user_dto)
            self.session.commit()
        except:
            raise

        return user_dto.to_entity()
