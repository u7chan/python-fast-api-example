import pytest

from app.domain.entity.user import User
from app.domain.repository.user_repository import UserRepository
from app.infrastructure.database.models import UserDto
from app.infrastructure.database.repository.user_repository_impl import (
    UserRepositoryImpl,
)
from app.tests.domain.repository.session_mock import SessionMock


class TestUserRepository:
    session: SessionMock
    repository: UserRepository

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.session = SessionMock()
        self.repository = UserRepositoryImpl(session=self.session)

    def test_should_be_fetch_empty(self):
        # Given
        self.session.all__mock.return_value([])

        # When
        actual = self.repository.fetch_all()

        # Then
        assert len(actual) == 0
        assert self.session.query__mock.called_with()[0] is UserDto
        assert self.session.limit__mock.called_with()[0] == 100
        assert self.session.all__mock.called_count() == 1

    def test_should_be_fetch_multiple_item(self):
        # Given
        users: [User] = [
            User(name="#name1", email="#email1"),
            User(name="#name2", email="#email2"),
        ]
        self.session.all__mock.return_value(
            list(map(lambda entity: UserDto.from_entity(entity), users))
        )

        # When
        actual = self.repository.fetch_all()

        # Then
        assert len(actual) == len(users)
        for i, expected in enumerate(users):
            assert actual[i] == expected

        assert self.session.query__mock.called_with()[0] is UserDto
        assert self.session.limit__mock.called_with()[0] == 100
        assert self.session.all__mock.called_count() == 1

    def test_should_be_insert_data(self):
        # Given
        user = User(name="#name", email="#email")
        excepted = UserDto.from_entity(user)

        # When
        self.repository.insert(user=user)

        # Then
        assert self.session.add__mock.called_count() == 1

        (actual,) = self.session.add__mock.called_with()
        assert actual.id != ""
        assert actual.name == excepted.name
        assert actual.email == excepted.email

    def test_should_be_update_data(self):
        # Given
        user = User(id="#id", name="#name", email="#email")
        excepted = UserDto.from_entity(user)
        self.session.one__mock.return_value(excepted)

        # When
        self.repository.update(user=user)

        # Then
        assert self.session.query__mock.called_with()[0] is UserDto
        assert self.session.filter_by__mock.called_with()[0] == {"id": user.id}
        assert self.session.one__mock.called_count() == 1
