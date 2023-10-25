from app.domain.repository.account_repository import AccountRepository
from app.domain.usecase.auth.create_account_usecase import CreateAccountCase


class CreateAccountCaseImpl(CreateAccountCase):
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def execute(self):
        pass
