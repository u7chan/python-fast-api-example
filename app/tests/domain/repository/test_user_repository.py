import pytest
from app.domain.entity.user import User

from app.domain.repository.user_repository import UserRepository, UserRepositoryImpl
from app.infrastructure.database.models import UserDto
from app.tests.domain.repository.session_mock import SessionMock


class TestUserRepository:
    session_mock: SessionMock
    repository: UserRepository

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.session_mock = SessionMock()
        self.repository = UserRepositoryImpl(session=self.session_mock)

    def test_should_be_fetch_empty(self):
        # Given
        excepted = []
        self.session_mock.all_value = excepted

        # When
        actual = self.repository.fetch_all()

        # Then
        assert actual == excepted

    def test_should_be_fetch_multiple_item(self):
        # Given
        users: [User] = [
            User(name="#name1", email="#email1"),
            User(name="#name2", email="#email2"),
        ]
        self.session_mock.all_value = list(
            map(lambda entity: UserDto.from_entity(entity), users)
        )

        # When
        actual = self.repository.fetch_all()

        # Then
        assert len(actual) == len(users)
        for i, expected in enumerate(users):
            assert actual[i] == expected

    def test_should_be_exception(self):
        # Given
        expected = "raise by test"
        self.session_mock.raise_query = Exception(expected)

        # When
        with pytest.raises(Exception) as actual:
            self.repository.fetch_all()

        # Then
        assert str(actual.value) == expected
