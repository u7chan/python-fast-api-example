from sqlalchemy.orm.session import Session

from app.domain.entity.account import Account
from app.domain.repository.account_repository import AccountRepository
from app.infrastructure.database.models import AccountDao


class AccountRepositoryImpl(AccountRepository):
    def __init__(self, session: Session):
        self.session = session

    def insert(self, account: Account) -> Account:
        account_dto = AccountDao.from_entity(account)
        self.session.add(account_dto)

        return account_dto.to_entity()
