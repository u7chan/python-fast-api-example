from typing import Optional

from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound

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

    def find_by_login_id(self, login_id) -> Optional[Account]:
        try:
            account_dto = (
                self.session.query(AccountDao).filter_by(login_id=login_id).one()
            )
        except NoResultFound:
            return None
        except:
            raise
        return account_dto.to_entity()
