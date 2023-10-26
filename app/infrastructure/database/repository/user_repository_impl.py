from uuid import uuid4
from sqlalchemy.orm.session import Session

from app.domain.entity.user import User
from app.domain.repository.user_repository import UserRepository
from app.infrastructure.database.models import UserDto


class UserRepositoryImpl(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def fetch_all(self) -> [User]:
        user_dtos = (
            self.session.query(UserDto)
            .order_by(UserDto.updated_at.desc())
            .limit(100)
            .all()
        )

        if len(user_dtos) == 0:
            return []

        return list(map(lambda dto: dto.to_entity(), user_dtos))

    def insert(self, user: User) -> User:
        user_dto = UserDto.from_entity(user)
        user_dto.id = str(uuid4())
        self.session.add(user_dto)
        return user_dto.to_entity()

    def update(self, user: User) -> User:
        user_dto = UserDto.from_entity(user)
        _user = self.session.query(UserDto).filter_by(id=user.id).one()
        _user.update_from_dto(user_dto)
        return user_dto.to_entity()
