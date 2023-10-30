from fastapi import APIRouter, Depends, Response, status

from app.domain.usecase.user.create_user_usecase import CreateUserUseCase
from app.presentation.auth.account.account_request import AccountRequest
from app.presentation.auth.account.account_response import AccountResponse
from app.presentation.auth.account.account_translator import AccountTranslator
from app.di.usecase import inject_create_user_usecase

router = APIRouter()


@router.post(
    path="/account",
    tags=["Auth"],
    status_code=status.HTTP_200_OK,
    response_model=AccountResponse,
)
async def create_account(
    request: AccountRequest,
    create_user_usecase: CreateUserUseCase = Depends(inject_create_user_usecase),
) -> AccountResponse:
    return AccountTranslator.entity_to_response(
        create_user_usecase.execute(AccountTranslator.request_to_entity(request))
    )
