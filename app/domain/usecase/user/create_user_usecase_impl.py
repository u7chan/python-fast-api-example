from app.domain.repository.user_repository import UserRepository
from app.domain.entity.user import User
from app.domain.usecase.user.create_user_usecase import CreateUserUseCase


class CreateUserUseCaseImpl(CreateUserUseCase):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, data: User) -> User:
        try:
            user = self.user_repository.insert(data)
        except:
            raise
        return user
