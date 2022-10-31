import typing

from strike_api.base import call_api


def get_account(
    account_id: typing.Optional[str],
    handle: typing.Optional[str],
) -> dict:
    """Fetch public account profile info by id or handle

    Args:
        account_id (typing.Optional[str]): Account id
        handle (typing.Optional[str]): Handle attached to the account to fetch

    Returns:
        dict: account schema

    """

    if account_id:
        url = f"https://api.strike.me/v1/accounts/{account_id}/profile"
    if handle:
        url = f"https://api.strike.me/v1/accounts/handle/{handle}/profile"

    return call_api("GET", url)
