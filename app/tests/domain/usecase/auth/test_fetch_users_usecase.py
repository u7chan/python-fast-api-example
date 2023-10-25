import pytest
from unittest.mock import Mock

from app.domain.entity.user import User
from app.domain.usecase.auth.create_account_usecase import CreateAccountCase
from app.domain.usecase.auth.create_account_usecase_impl import CreateAccountCaseImpl


class TestCreateAccountCase:
    user_repository_mock: Mock
    usecase: CreateAccountCase

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.user_repository_mock = Mock()
        self.usecase = CreateAccountCaseImpl(
            account_repository=self.user_repository_mock
        )

    def test_should_be_create_account(self):
        # Given

        # When
        self.usecase.execute()

        # Then
