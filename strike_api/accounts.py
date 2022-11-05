import typing

from strike_api.base import call_api
from strike_api.models.accounts import Account


def get_account(
    account_id: typing.Optional[str] = None,
    handle: typing.Optional[str] = None,
) -> Account:
    """Fetch public account profile info by id or handle

    Args:
        account_id (typing.Optional[str]): Account id
        handle (typing.Optional[str]): Handle attached to the account to fetch

    Returns:
        dict: account schema
    """

    url = ""
    if account_id and not handle:
        url = f"https://api.strike.me/v1/accounts/{account_id}/profile"
    elif handle and not account_id:
        url = f"https://api.strike.me/v1/accounts/handle/{handle}/profile"
    else:
        raise ValueError("use either account_id or handle")

    response = call_api("GET", url)
    return Account.parse_obj(response)
