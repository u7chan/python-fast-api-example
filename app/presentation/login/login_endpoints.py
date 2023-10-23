from fastapi import APIRouter, Depends, Response, status

from app.domain.usecase.login_usecase import LoginUseCase
from app.presentation.login.login_request import LoginRequest
from app.presentation.login.login_response import LoginResponse
from app.presentation.login.login_translator import LoginTranslator
from app.di.usecase import inject_login_usecase

router = APIRouter()


@router.post(
    path="/login",
    tags=["Auth"],
    status_code=status.HTTP_200_OK,
    response_model=LoginResponse,
)
async def login(
    request: LoginRequest,
    response: Response,
    login_usecase: LoginUseCase = Depends(inject_login_usecase),
):
    session = login_usecase.execute(LoginTranslator.request_to_entity(request))
    response.set_cookie(
        key="session",
        value=session.id,
        expires=session.expires.strftime("%a, %d-%b-%Y %T GMT"),
    )
    return LoginTranslator.entity_to_response(session)
