from app.domain.entity.user import (
    User,
)
from app.presentation.user.user_request import (
    UserRequest,
)
from app.presentation.user.user_response import (
    UserModel,
    UserResponse,
)


class UserTranslator:
    @staticmethod
    def request_to_entity(
        request: UserRequest,
    ) -> User:
        return User(
            id="TODO",
            name="TODO",
            email="TODO",
        )

    @staticmethod
    def entities_to_response(
        entities: [User],
    ) -> UserResponse:
        return UserResponse(
            data=list(
                map(
                    lambda it: UserTranslator.__user_to_user_model(it),
                    entities,
                )
            )
        )

    @staticmethod
    def __user_to_user_model(user: User) -> UserModel:
        return UserModel(
            id=user.id,
            name=user.name,
            email=user.email,
            updated_at=str(user.updated_at),
        )
