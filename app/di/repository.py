from fastapi import Depends
from sqlalchemy.orm import Session

from app.infrastructure.database.session import get_session
from app.domain.repository.user_repository import UserRepository, UserRepositoryImpl


def inject_user_repository(session: Session = Depends(get_session)) -> UserRepository:
    return UserRepositoryImpl(session=session)
