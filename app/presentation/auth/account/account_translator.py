from app.domain.entity.account import Account
from app.presentation.auth.account.account_request import AccountRequest
from app.presentation.auth.account.account_response import AccountResponse


class AccountTranslator:
    @staticmethod
    def request_to_entity(
        request: AccountRequest,
    ) -> Account:
        return Account(user_id="", login_id=request.login_id, password=request.password)

    @staticmethod
    def entity_to_response(account: Account) -> AccountResponse:
        return AccountResponse(user_id=account.user_id)
