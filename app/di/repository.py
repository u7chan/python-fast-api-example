from fastapi import Depends
from sqlalchemy.orm import Session

from app.infrastructure.database import get_session
from app.domain.repository import UserRepository, UserRepositoryImpl


def inject_user_repository(session: Session = Depends(get_session)) -> UserRepository:
    return UserRepositoryImpl(session=session)
