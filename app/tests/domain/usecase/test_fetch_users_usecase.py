import pytest
from unittest.mock import Mock

from app.domain.entity.user import User
from app.domain.usecase.user.create_user_usecase import CreateUserUseCase
from app.domain.usecase.user.create_user_usecase_impl import CreateUserUseCaseImpl


class TestFetchUsersUseCase:
    user_repository_mock: Mock
    usecase: CreateUserUseCase

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.user_repository_mock = Mock()
        self.usecase = CreateUserUseCaseImpl(user_repository=self.user_repository_mock)

    def test_should_be_create_user(self):
        # Given
        expected = User(id="#id", name="#name", email="#email")
        self.user_repository_mock.save.return_value = expected

        # When
        actual = self.usecase.execute(data=expected)

        # Then
        self.user_repository_mock.save.assert_called_once()
        assert actual == expected

    def test_should_be_exception(self):
        # Given
        expected = "raise by test"
        self.user_repository_mock.save.side_effect = Exception(expected)

        # When
        with pytest.raises(Exception) as actual:
            self.usecase.execute(data=User(name="#name", email="#email"))

        # Then
        self.user_repository_mock.save.assert_called_once()
        assert str(actual.value) == expected
