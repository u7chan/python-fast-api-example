from fastapi import APIRouter, Depends, HTTPException, status

from app.domain.exception.duplication_exception import DuplicationException
from app.domain.usecase.auth.create_account_usecase import CreateAccountUseCase
from app.presentation.auth.account.account_request import AccountRequest
from app.presentation.auth.account.account_response import (
    AccountResponse,
    ErrorMessageAccountAlreadyExists,
)
from app.presentation.auth.account.account_translator import AccountTranslator
from app.di.usecase import inject_create_account_usecase

router = APIRouter()


@router.post(
    path="/account",
    tags=["Auth"],
    status_code=status.HTTP_201_CREATED,
    response_model=AccountResponse,
    responses={
        status.HTTP_409_CONFLICT: {
            "model": ErrorMessageAccountAlreadyExists,
        },
    },
)
async def create_account(
    request: AccountRequest,
    create_account_usecase: CreateAccountUseCase = Depends(
        inject_create_account_usecase
    ),
) -> AccountResponse:
    try:
        account = create_account_usecase.execute(
            AccountTranslator.request_to_entity(request)
        )
    except DuplicationException as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    return AccountTranslator.entity_to_response(account)
