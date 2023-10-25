from uuid import uuid4
from sqlalchemy.orm.session import Session

from app.domain.entity.user import User
from app.domain.repository.user_repository import UserRepository
from app.infrastructure.database.models import UserDto


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
            user_dto = UserDto.from_entity(user)
            if user.id is None:
                user_dto.id = str(uuid4())
                self.session.add(user_dto)
            else:
                _user = self.session.query(UserDto).filter_by(id=user.id).one()
                _user.update_from_dto(user_dto)
            self.session.commit()  # TODO: Delete this line by unit of work
        except:
            raise

        return user_dto.to_entity()
