from fastapi import Depends

from app.domain.repository import UserRepository
from app.domain.usecase import (
    CreateUserUseCase,
    CreateUserUseCaseImpl,
    FetchUsersUseCase,
    FetchUsersUseCaseImpl,
)
from app.di.repository import inject_user_repository


def inject_create_user_usecase(
    user_repository: UserRepository = Depends(inject_user_repository),
) -> CreateUserUseCase:
    return CreateUserUseCaseImpl(user_repository=user_repository)


def inject_fetch_users_usecase(
    user_repository: UserRepository = Depends(inject_user_repository),
) -> FetchUsersUseCase:
    return FetchUsersUseCaseImpl(user_repository=user_repository)
