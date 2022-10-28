from base import call_api


def get_event(
    event_id: str,
) -> dict:
    url = "https://api.strike.me/v1/events/:eventId"

    return call_api("GET", url)


def get_events(
    filter: str = None, orderby: str = None, skip: int = None, top: int = None
):
    url = "https://api.strike.me/v1/events"

    payload = {}

    return call_api("GET", url, data=payload)
