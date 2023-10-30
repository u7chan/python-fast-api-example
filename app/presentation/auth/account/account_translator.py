from app.domain.entity.account import Account
from app.domain.entity.create_account import CreateAccount
from app.presentation.auth.account.account_request import AccountRequest
from app.presentation.auth.account.account_response import AccountResponse


class AccountTranslator:
    @staticmethod
    def request_to_entity(
        request: AccountRequest,
    ) -> CreateAccount:
        return CreateAccount(
            name=request.name, email=request.email, password=request.password
        )

    @staticmethod
    def entity_to_response(account: Account) -> AccountResponse:
        return AccountResponse(user_id=account.user_id)
