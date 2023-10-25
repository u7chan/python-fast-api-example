from app.domain.entity.account import Account
from app.domain.entity.create_account import CreateAccount
from app.domain.entity.user import User
from app.domain.repository.account_repository import AccountRepository
from app.domain.repository.user_repository import UserRepository
from app.domain.usecase.auth.create_account_usecase import CreateAccountCase


class CreateAccountCaseImpl(CreateAccountCase):
    def __init__(
        self, user_repository: UserRepository, account_repository: AccountRepository
    ):
        self.user_repository = user_repository
        self.account_repository = account_repository

    def execute(self, create_account: CreateAccount):
        try:
            user = self.user_repository.save(
                User(name=create_account.name, email=create_account.email)
            )
            self.account_repository.insert(
                Account(
                    user_id=user.id,
                    login_id=user.email,
                    password=create_account.password,
                )
            )
        except:
            raise
