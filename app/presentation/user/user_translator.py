from app.domain.entity.user import User
from app.presentation.user.user_request import UserRequest
from app.presentation.user.user_response import UserResponse, UsersResponse


class UserTranslator:
    @staticmethod
    def request_to_entity(
        request: UserRequest,
    ) -> User:
        return User(name=request.name, email=request.email)

    @staticmethod
    def entity_to_response(user: User) -> UserResponse:
        return UserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            updated_at=str(user.updated_at),
        )

    @staticmethod
    def entities_to_response(
        entities: [User],
    ) -> UsersResponse:
        return UsersResponse(
            data=list(
                map(
                    lambda it: UserTranslator.entity_to_response(it),
                    entities,
                )
            )
        )
