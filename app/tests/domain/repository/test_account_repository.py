import pytest

from sqlalchemy.exc import NoResultFound

from app.domain.entity.account import Account
from app.domain.repository.account_repository import AccountRepository
from app.infrastructure.database.models import AccountDto
from app.infrastructure.database.repository.account_repository_impl import (
    AccountRepositoryImpl,
)
from app.tests.domain.repository.session_mock import SessionMock


class TestAccountRepository:
    session: SessionMock
    repository: AccountRepository

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.session = SessionMock()
        self.repository = AccountRepositoryImpl(session=self.session)

    def test_should_be_insert_data(self):
        # Given
        account = Account(
            user_id="#user_id", login_id="#login_id", password="#password"
        )
        excepted = AccountDto.from_entity(account)

        # When
        self.repository.insert(account=account)

        # Then
        assert self.session.add__mock.called_count() == 1

        (actual,) = self.session.add__mock.called_with()
        assert actual.user_id == excepted.user_id
        assert actual.login_id == excepted.login_id
        assert actual.password_hash == excepted.password_hash

    def test_should_be_find_by_login_id(self):
        # Given
        excepted = Account(
            user_id="#user_id", login_id="#login_id", password="#password"
        )
        self.session.one__mock.return_value(AccountDto.from_entity(excepted))

        # When
        actual = self.repository.find_by_login_id(login_id="#login_id")

        # Then
        assert actual == excepted

    def test_should_be_find_by_login_id_not_found(self):
        # Given
        excepted = None
        self.session.one__mock.raise_error(NoResultFound)

        # When
        actual = self.repository.find_by_login_id(login_id="#login_id")

        # Then
        assert actual == excepted

    def test_should_be_find_by_login_id_exception(self):
        # Given
        excepted = "test"
        self.session.one__mock.raise_error(Exception(excepted))

        # When
        with pytest.raises(Exception) as actual:
            self.repository.find_by_login_id(login_id="#login_id")

        # Then
        assert str(actual.value) == excepted
