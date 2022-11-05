import os
import typing
import requests


def set_default_headers(
    headers: typing.Optional[typing.Dict[str, str]] = None
) -> typing.Dict[str, str]:
    """Sets the default headers for strike api HTTP requests

    Args:
        headers (typing.Optional[dict], optional): HTTP Headers. Defaults to None.

    Returns:
        dict: headers with default headers included
    """
    strike_api_key = os.environ.get("STRIKE_API_KEY")
    if not strike_api_key:
        raise EnvironmentError("STRIKE_API_KEY not found in environment variables")

    if not headers:
        headers = {}

    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {strike_api_key}"

    return headers


def call_api(
    method: str,
    url: str,
    headers: typing.Optional[typing.Dict[str, str]] = None,
    params: typing.Optional[typing.Union[typing.Dict[str, typing.Any], str]] = None,
    data: typing.Optional[typing.Union[typing.Dict[str, str], str]] = None,
) -> typing.Union[
    typing.Dict[str, typing.Any], typing.List[typing.Dict[str, typing.Any]]
]:
    """Generic method to interact with strike API endpoints

    Args:
        method (str): HTTP Method
        url (str): Fully qualifed url to interact with a strike endpoint
        headers (typing.Optional[dict], optional): HTTP Headers. Defaults to None.
        params (typing.Optional[typing.Union[dict, str]], optional): params to pass to Strike as query string. Defaults to None.
        data (typing.Optional[typing.Union[dict, str]], optional): Data to pass to Strike as body. Defaults to None.

    Raises:
        EnvironmentError: The Strike API key must be in env

    Returns:
        typing.Any: response from api call
    """

    headers = set_default_headers(headers)
    response = requests.request(method, url, headers=headers, params=params, data=data)
    response.raise_for_status()

    if response.content:
        return response.json()
    else:
        return {}
