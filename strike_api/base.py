import os
import typing
import requests


def call_api(
    method: str,
    url: str,
    headers: typing.Optional[dict] = None,
    data: typing.Optional[typing.Union[dict, str]] = None,
) -> typing.Union[typing.List[dict], dict]:
    """Generic method to interact with strike API endpoints

    Args:
        method (str): HTTP Method
        url (str): Fully qualifed url to interact with a strike endpoint
        headers (typing.Optional[dict], optional): HTTP Headers. Defaults to None.
        data (typing.Optional[typing.Union[dict, str]], optional): Data to pass to Strike. Defaults to None.

    Raises:
        EnvironmentError: The Strike API key must be in env

    Returns:
        dict: response from api call
    """
    strike_api_key = os.environ.get("STRIKE_API_KEY")
    if not strike_api_key:
        raise EnvironmentError("STRIKE_API_KEY not found in environment variables")

    if not headers:
        headers = {}

    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {strike_api_key}"

    response = requests.request(method, url, headers=headers, data=data)

    return response.json()
