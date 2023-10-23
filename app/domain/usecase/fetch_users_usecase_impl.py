from app.domain.repository.user_repository import UserRepository
from app.domain.entity.user import User
from app.domain.usecase.fetch_users_usecase import FetchUsersUseCase


class FetchUsersUseCaseImpl(FetchUsersUseCase):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self) -> [User]:
        try:
            users = self.user_repository.fetch_all()
        except:
            raise
        return users
