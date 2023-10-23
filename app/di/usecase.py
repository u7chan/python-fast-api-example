from fastapi import Depends

from app.domain.usecase.create_user_usecase import CreateUserUseCase
from app.domain.usecase.create_user_usecase_impl import CreateUserUseCaseImpl
from app.domain.usecase.fetch_users_usecase import FetchUsersUseCase
from app.domain.usecase.fetch_users_usecase_impl import FetchUsersUseCaseImpl
from app.domain.repository.user_repository import UserRepository
from app.di.repository import inject_user_repository


def inject_create_user_usecase(
    user_repository: UserRepository = Depends(inject_user_repository),
) -> CreateUserUseCase:
    return CreateUserUseCaseImpl(user_repository=user_repository)


def inject_fetch_users_usecase(
    user_repository: UserRepository = Depends(inject_user_repository),
) -> FetchUsersUseCase:
    return FetchUsersUseCaseImpl(user_repository=user_repository)
