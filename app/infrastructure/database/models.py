from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import as_declarative, declared_attr
from app.domain.entity.account import Account

from app.domain.entity.user import User


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
    __tablename__ = "user"

    id = Column(String, primary_key=True, autoincrement=False, nullable=False)
    name = Column(String, default="", nullable=False)
    email = Column(String, default="", nullable=False)

    def to_entity(self) -> User:
        return User(
            id=self.id,
            name=self.name,
            email=self.email,
            updated_at=self.updated_at,
        )

    def update_from_dto(self, user_dto: "UserDto"):
        self.name = user_dto.name
        self.email = user_dto.email

    @staticmethod
    def from_entity(user: User) -> "UserDto":
        return UserDto(
            id=user.id,
            name=user.name,
            email=user.email,
        )


class AccountDao(Base):
    __tablename__ = "account"

    user_id = Column(ForeignKey("user.id"), nullable=True)
    login_id = Column(String, primary_key=True, autoincrement=False, nullable=False)
    password_hash = Column(String, default="", nullable=False)

    def to_entity(self) -> Account:
        return Account(
            user_id=self.user_id,
            login_id=self.login_id,
            password_hash=self.password_hash,
        )

    @staticmethod
    def from_entity(account: Account) -> "AccountDao":
        return UserDto(
            user_id=account.user_id,
            login_id=account.login_id,
            password_hash=account.password_hash,
        )
