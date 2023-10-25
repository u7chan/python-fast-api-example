import pytest

from app.domain.entity.account import Account
from app.domain.repository.account_repository import AccountRepository
from app.infrastructure.database.models import AccountDao
from app.infrastructure.database.repository.account_repository_impl import (
    AccountRepositoryImpl,
)
from app.tests.domain.repository.session_mock import SessionMock


class TestAccountRepository:
    session_mock: SessionMock
    repository: AccountRepository

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.session_mock = SessionMock()
        self.repository = AccountRepositoryImpl(session=self.session_mock)

    def test_should_be_append_data(self):
        # Given
        account = Account(user_id="a", login_id="b", password="c")
        excepted = AccountDao.from_entity(account)

        # When
        actual = self.repository.insert(account=account)
        add_args = self.session_mock.add_value

        # Then
        assert self.session_mock.add_call_count == 1

        assert actual.user_id == excepted.user_id
        assert actual.login_id == excepted.login_id
        assert actual.password == excepted.password_hash

        assert add_args.user_id == excepted.user_id
        assert add_args.login_id == excepted.login_id
        assert add_args.password_hash == excepted.password_hash
