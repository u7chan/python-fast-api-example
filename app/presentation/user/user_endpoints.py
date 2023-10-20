from fastapi import APIRouter, Depends, status

from app.domain.usecase.create_user_usecase import CreateUserUseCase
from app.domain.usecase.fetch_users_usecase import FetchUsersUseCase
from app.presentation.user.user_request import UserRequest
from app.presentation.user.user_response import UserResponse, UsersResponse
from app.presentation.user.user_translator import UserTranslator
from app.di.usecase import inject_create_user_usecase, inject_fetch_users_usecase

router = APIRouter()


@router.post(
    path="/user",
    tags=["User"],
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse,
)
async def create_user(
    request: UserRequest,
    create_user_usecase: CreateUserUseCase = Depends(inject_create_user_usecase),
) -> UserResponse:
    return UserTranslator.entity_to_response(
        create_user_usecase.execute(UserTranslator.request_to_entity(request))
    )


@router.get(
    path="/users",
    tags=["User"],
    status_code=status.HTTP_200_OK,
    response_model=UsersResponse,
)
async def fetch_users(
    fetch_users_usecase: FetchUsersUseCase = Depends(inject_fetch_users_usecase),
) -> UsersResponse:
    return UserTranslator.entities_to_response(fetch_users_usecase.execute())
