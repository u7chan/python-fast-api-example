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
        self.session_mock.all_return_value = excepted

        # When
        actual = self.repository.fetch_all()

        # Then
        assert self.session_mock.all_call_count == 1
        assert actual == excepted

    def test_should_be_fetch_multiple_item(self):
        # Given
        users: [User] = [
            User(name="#name1", email="#email1"),
            User(name="#name2", email="#email2"),
        ]
        self.session_mock.all_return_value = list(
            map(lambda entity: UserDto.from_entity(entity), users)
        )

        # When
        actual = self.repository.fetch_all()

        # Then
        assert self.session_mock.all_call_count == 1
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

    def test_should_be_append_data(self):
        # Given
        user = User(name="#name", email="#email")
        excepted = UserDto.from_entity(user)

        # When
        actual = self.repository.save(user=user)
        add_args = self.session_mock.add_value

        # Then
        assert self.session_mock.add_call_count == 1
        assert self.session_mock.commit_call_count == 1
        assert actual.id == add_args.id
        assert actual.name == excepted.name
        assert actual.email == excepted.email
        assert add_args.name == excepted.name
        assert add_args.email == excepted.email

    def test_should_be_update_data(self):
        # Given
        user = User(id="#id", name="#name", email="#email")
        excepted = UserDto.from_entity(user)
        self.session_mock.one_return_value = excepted

        # When
        actual = self.repository.save(user=user)

        # Then
        assert self.session_mock.one_call_count == 1
        assert self.session_mock.commit_call_count == 1
        assert actual.name == excepted.name
        assert actual.email == excepted.email
