from fastapi import APIRouter, Depends, status

from app.domain.usecase import CreateUserUseCase, FetchUsersUseCase
from app.presentation.user.user_response import UserResponse
from app.di import inject_create_user_usecase, inject_fetch_users_usecase


router = APIRouter()


@router.post(
    path="/user",
    tags=["user"],
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    create_user_usecase: CreateUserUseCase = Depends(inject_create_user_usecase),
):
    return create_user_usecase.execute()


@router.get(path="/users", tags=["user"], status_code=status.HTTP_200_OK)
async def fetch_users(
    fetch_users_usecase: FetchUsersUseCase = Depends(inject_fetch_users_usecase),
) -> UserResponse:
    data = fetch_users_usecase.execute()
    return UserResponse.from_entity(data)
