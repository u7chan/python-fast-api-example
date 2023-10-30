from app.domain.entity.account import Account
from app.domain.entity.create_account import CreateAccount
from app.domain.entity.user import User
from app.domain.repository.account_repository import AccountRepository
from app.domain.repository.user_repository import UserRepository
from app.domain.unitofwork.unit_of_work import UnitOfWork
from app.domain.usecase.auth.create_account_usecase import CreateAccountUseCase


class CreateAccountUseCaseImpl(CreateAccountUseCase):
    def __init__(
        self,
        user_repository: UserRepository,
        account_repository: AccountRepository,
        uow: UnitOfWork,
    ):
        self.user_repository = user_repository
        self.account_repository = account_repository
        self.uow = uow

    def execute(self, data: CreateAccount):
        try:
            self.uow.begin()
            user = self.user_repository.insert(User(name=data.name, email=data.email))
            account = Account(
                user_id=user.id,
                login_id=user.email,
                password=data.password,
            )
            self.account_repository.insert(account)
            self.uow.commit()
            return account
        except:
            self.uow.rollback()
            raise
