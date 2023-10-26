from app.domain.repository.user_repository import UserRepository
from app.domain.entity.user import User
from app.domain.unitofwork.unit_of_work import UnitOfWork
from app.domain.usecase.user.create_user_usecase import CreateUserUseCase


class CreateUserUseCaseImpl(CreateUserUseCase):
    def __init__(self, user_repository: UserRepository, uow: UnitOfWork):
        self.user_repository = user_repository
        self.uow = uow

    def execute(self, data: User) -> User:
        try:
            self.uow.begin()
            user = self.user_repository.insert(data)
            self.uow.commit()
        except:
            self.uow.rollback()
            raise
        return user
