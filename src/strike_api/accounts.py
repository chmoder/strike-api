import typing

from base import call_api


def get_account(
    account_id: typing.Optional[str],
    handle: typing.Optional[str],
) -> dict:
    if account_id:
        url = f"https://api.strike.me/v1/accounts/{account_id}/profile"
    if handle:
        url = f"https://api.strike.me/v1/accounts/handle/{handle}/profile"

    return call_api("GET", url)
