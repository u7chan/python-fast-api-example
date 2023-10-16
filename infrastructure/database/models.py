from datetime import datetime

from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import as_declarative, declared_attr

from domain.value_object.user import User


@as_declarative()
class Base:
    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=datetime.now(), nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
        )


class UserDto(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)

    def to_entity(self) -> User:
        return User(
            id=self.id,
            name=self.name,
            email=self.email,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(user: User) -> "UserDto":
        return (
            UserDto(
                id=user.id,
                name=user.name,
                email=user.email,
            ),
        )
