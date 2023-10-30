import pytest
from unittest.mock import Mock, call

from app.domain.entity.account import Account
from app.domain.entity.create_account import CreateAccount
from app.domain.entity.user import User
from app.domain.exception.duplication_exception import DuplicationException
from app.domain.usecase.auth.create_account_usecase import CreateAccountUseCase
from app.domain.usecase.auth.create_account_usecase_impl import CreateAccountUseCaseImpl


class TestCreateAccountUseCase:
    user_repository: Mock
    account_repository: Mock
    uow: Mock
    usecase: CreateAccountUseCase

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.user_repository = Mock()
        self.account_repository = Mock()
        self.uow = Mock()
        self.usecase = CreateAccountUseCaseImpl(
            user_repository=self.user_repository,
            account_repository=self.account_repository,
            uow=self.uow,
        )

    def test_should_be_create_account(self):
        # Given
        create_account = CreateAccount(
            name="#name", email="#email", password="#password"
        )
        self.account_repository.find_by_login_id.return_value = None
        self.user_repository.insert.return_value = User(
            id="#user_id",
            name="#user_name",
            email="#user_email",
        )

        # When
        self.usecase.execute(create_account)

        # Then
        assert self.account_repository.find_by_login_id.call_args_list[0] == call(
            "#email"
        )
        assert self.user_repository.insert.call_args_list[0] == call(
            User(
                name="#name",
                email="#email",
            )
        )
        assert self.account_repository.insert.call_args_list[0] == call(
            Account(user_id="#user_id", login_id="#email", password="#password")
        )
        assert self.uow.commit.called == 1

    def test_should_be_exception(self):
        # Given
        expected = DuplicationException().message
        self.account_repository.find_by_login_id.return_value = Account(
            user_id="#user_id", login_id="#login_id"
        )

        # When
        with pytest.raises(DuplicationException) as actual:
            self.usecase.execute(
                CreateAccount(name="#name", email="#email", password="#password")
            )

        # Then
        assert self.account_repository.find_by_login_id.called == 1
        assert self.uow.rollback.called == 1
        assert str(actual.value) == expected
