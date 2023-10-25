import pytest
from unittest.mock import Mock

from app.domain.entity.create_account import CreateAccount
from app.domain.usecase.auth.create_account_usecase import CreateAccountCase
from app.domain.usecase.auth.create_account_usecase_impl import CreateAccountCaseImpl


class TestCreateAccountCase:
    user_repository_mock: Mock
    account_repository_mock: Mock
    usecase: CreateAccountCase

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.user_repository_mock = Mock()
        self.account_repository_mock = Mock()
        self.usecase = CreateAccountCaseImpl(
            user_repository=self.user_repository_mock,
            account_repository=self.account_repository_mock,
        )

    def test_should_be_create_account(self):
        # Given
        create_account = CreateAccount(
            name="#name", email="#email", password="#password"
        )

        # When
        self.usecase.execute(create_account)

        # Then
