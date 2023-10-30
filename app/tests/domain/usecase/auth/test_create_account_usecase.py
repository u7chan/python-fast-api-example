import pytest
from unittest.mock import Mock

from app.domain.entity.create_account import CreateAccount
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

        # When
        self.usecase.execute(create_account)

        # Then
        assert self.user_repository.insert.called == 1
        assert self.account_repository.insert.called == 1
        assert self.uow.begin.called == 1
        assert self.uow.commit.called == 1

    def test_should_be_exception(self):
        # Given
        expected = "raise by test"
        self.user_repository.insert.side_effect = Exception(expected)

        # When
        with pytest.raises(Exception) as actual:
            self.usecase.execute(
                CreateAccount(name="#name", email="#email", password="#password")
            )

        # Then
        assert self.user_repository.insert.called == 1
        assert self.uow.rollback.called == 1
        assert str(actual.value) == expected
