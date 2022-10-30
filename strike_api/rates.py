from strike_api.base import call_api


def get_ticker() -> dict:
    """Get currency exchange rate tickers

    Response will include list of all possible pairs for the following currencies: BTC, USD, USDT

    Returns:
        dict: ticker rates
    """
    url = f"https://api.strike.me/v1/rates/ticker"

    return call_api("GET", url)
