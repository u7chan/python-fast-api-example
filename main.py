from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from infrastructure.database import get_session
from domain.repository import UserRepository, UserRepositoryImpl
from domain.usecase import FetchUsersUseCase, FetchUsersUseCaseImpl


app = FastAPI()


def inject_user_repository(session: Session = Depends(get_session)) -> UserRepository:
    return UserRepositoryImpl(session=session)


def inject_fetch_users_usecase(
    user_repository: UserRepository = Depends(inject_user_repository),
) -> FetchUsersUseCase:
    return FetchUsersUseCaseImpl(user_repository=user_repository)


@app.get("/health-check")
async def health_check():
    return {"message": "OK"}


@app.get("/users")
async def get_users(
    fetch_users_usecase: FetchUsersUseCase = Depends(inject_fetch_users_usecase),
):
    return fetch_users_usecase.execute()
