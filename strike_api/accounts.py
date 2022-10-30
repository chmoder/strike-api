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


def test():
    r"""Sends a HEAD request.
    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes. If
        `allow_redirects` is not provided, it will be set to `False` (as
        opposed to the default :meth:`request` behavior).
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """
    
    pass