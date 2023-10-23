from app.domain.entity.login import Login
from app.domain.entity.session import Session
from app.presentation.login.login_request import LoginRequest
from app.presentation.login.login_response import LoginResponse


class LoginTranslator:
    @staticmethod
    def request_to_entity(
        request: LoginRequest,
    ) -> Login:
        return Login(id=request.login, password=request.password)

    @staticmethod
    def entity_to_response(session: Session) -> LoginResponse:
        return LoginResponse(expires=str(session.expires))
