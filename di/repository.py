from fastapi import Depends
from sqlalchemy.orm import Session

from infrastructure.database import get_session
from domain.repository import UserRepository, UserRepositoryImpl


def inject_user_repository(session: Session = Depends(get_session)) -> UserRepository:
    return UserRepositoryImpl(session=session)
