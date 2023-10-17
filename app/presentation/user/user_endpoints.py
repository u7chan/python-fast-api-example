from fastapi import APIRouter, Depends, status

from app.domain.usecase import CreateUserUseCase, FetchUsersUseCase
from app.presentation.user.user_response import UserResponse
from app.presentation.user.user_translator import UserTranslator
from app.di import inject_create_user_usecase, inject_fetch_users_usecase

router = APIRouter()


@router.post(
    path="/user",
    tags=["User"],
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    create_user_usecase: CreateUserUseCase = Depends(inject_create_user_usecase),
):
    return create_user_usecase.execute()


@router.get(
    path="/users",
    tags=["User"],
    status_code=status.HTTP_200_OK,
    response_model=UserResponse,
)
async def fetch_users(
    fetch_users_usecase: FetchUsersUseCase = Depends(inject_fetch_users_usecase),
) -> UserResponse:
    return UserTranslator.entities_to_response(fetch_users_usecase.execute())
