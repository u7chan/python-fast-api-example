from fastapi import Depends

from app.domain.unitofwork.unit_of_work import UnitOfWork
from app.domain.usecase.user.create_user_usecase import CreateUserUseCase
from app.domain.usecase.user.create_user_usecase_impl import CreateUserUseCaseImpl
from app.domain.usecase.user.fetch_users_usecase import FetchUsersUseCase
from app.domain.usecase.user.fetch_users_usecase_impl import FetchUsersUseCaseImpl
from app.domain.usecase.auth.login_usecase import LoginUseCase
from app.domain.usecase.auth.login_usecase_impl import LoginUseCaseImpl
from app.domain.repository.user_repository import UserRepository
from app.domain.repository.session_repository import SessionRepository
from app.di.unit_of_work import inject_unit_of_work
from app.di.repository import inject_session_repository, inject_user_repository


def inject_create_user_usecase(
    user_repository: UserRepository = Depends(inject_user_repository),
    uow: UnitOfWork = Depends(inject_unit_of_work),
) -> CreateUserUseCase:
    return CreateUserUseCaseImpl(user_repository=user_repository, uow=uow)


def inject_fetch_users_usecase(
    user_repository: UserRepository = Depends(inject_user_repository),
) -> FetchUsersUseCase:
    return FetchUsersUseCaseImpl(user_repository=user_repository)


def inject_login_usecase(
    session_repository: SessionRepository = Depends(inject_session_repository),
) -> LoginUseCase:
    return LoginUseCaseImpl(session_repository=session_repository)
