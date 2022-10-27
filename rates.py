from base import call_api


def get_ticker() -> dict:
    url = f"https://api.strike.me/v1/rates/ticker"

    return call_api("GET", url)
