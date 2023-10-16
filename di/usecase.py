from fastapi import Depends

from domain.repository import UserRepository
from domain.usecase import FetchUsersUseCase, FetchUsersUseCaseImpl
from di.repository import inject_user_repository


def inject_fetch_users_usecase(
    user_repository: UserRepository = Depends(inject_user_repository),
) -> FetchUsersUseCase:
    return FetchUsersUseCaseImpl(user_repository=user_repository)
