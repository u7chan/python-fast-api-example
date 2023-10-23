from app.domain.entity.login import Login
from app.presentation.login.login_request import LoginRequest


class LoginTranslator:
    @staticmethod
    def request_to_entity(
        request: LoginRequest,
    ) -> Login:
        return Login(id=request.login, password=request.password)
