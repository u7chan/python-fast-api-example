from app.domain.entity.account import Account
from app.domain.entity.create_account import CreateAccount
from app.domain.entity.user import User
from app.domain.exception.duplication_exception import DuplicationException
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
        login_id = data.email
        try:
            self.uow.begin()
            if self.account_repository.find_by_login_id(login_id) is not None:
                raise DuplicationException()

            user = self.user_repository.insert(User(name=data.name, email=data.email))
            account = Account(
                user_id=user.id,
                login_id=login_id,
                password=data.password,
            )
            self.account_repository.insert(account)
            self.uow.commit()

            return account
        except:
            self.uow.rollback()
            raise
