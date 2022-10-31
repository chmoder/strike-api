import typing
from strike_api.base import call_api


def get_event(
    event_id: str,
) -> dict:
    """Find event by id

    Args:
        event_id (str): Event id

    Returns:
        dict: event schema
    """
    url = "https://api.strike.me/v1/events/:eventId"

    return call_api("GET", url)


def get_events(
    filter: str = None, orderby: str = None, skip: int = None, top: int = None
) -> typing.List[dict]:
    """Get Events
    Required scopes: partner.webhooks.manage
    OData filtering syntax can be seen `here <https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-odata/7d6c4117-317d-4860-915b-7e321be017e3>`_.  Ordering syntax can be seen `here <https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-odata/793b1e83-95ee-4446-8434-f5b634f20d1e>`_.

    Args:
        filter (str, optional): Filter the results using OData syntax. Supported properties: created, eventType, deliverySuccess. Defaults to None.
        orderby (str, optional): Order the results using OData syntax. Supported properties: created. Defaults to None.
        skip (int, optional): Skip the specified number of entries. Defaults to None.
        top (int, optional): Get the top X number of records. Default value: 50. Max value: 100. Defaults to None.

    Returns:
        typing.List[dict]: events
    """
    url = "https://api.strike.me/v1/events"

    payload = {}

    return call_api("GET", url, data=payload)
