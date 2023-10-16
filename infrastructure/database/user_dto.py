from domain.value_object.user import User
from infrastructure.database.models import UserEntity


class UserDto:
    @staticmethod
    def to_entity(user: User) -> UserEntity:
        return (
            UserEntity(
                id=user.id,
                name=user.name,
                email=user.email,
            ),
        )

    @staticmethod
    def from_entity(entity: UserEntity) -> User:
        return User(
            id=entity.id,
            name=entity.name,
            email=entity.email,
            updated_at=entity.updated_at,
        )
