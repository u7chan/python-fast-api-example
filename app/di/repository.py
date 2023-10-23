from fastapi import Depends
from sqlalchemy.orm import Session

from app.infrastructure.database.session import get_session
from app.infrastructure.database.repository.user_repository_impl import (
    UserRepositoryImpl,
)
from app.domain.repository.user_repository import UserRepository
from app.domain.repository.session_repository import (
    SessionRepository,
    SessionRepositoryInMemory,
)


def inject_user_repository(session: Session = Depends(get_session)) -> UserRepository:
    return UserRepositoryImpl(session=session)


def inject_session_repository() -> SessionRepository:
    return SessionRepositoryInMemory()
