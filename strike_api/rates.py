from strike_api.base import call_api
from strike_api.models.rates import Rates


def get_ticker() -> Rates:
    """Get currency exchange rate tickers

    Response will include list of all possible pairs for the following currencies: BTC, USD, USDT

    Returns:
        dict: ticker rates
    """
    url = f"https://api.strike.me/v1/rates/ticker"

    response = call_api("GET", url)
    return Rates.parse_obj(response)
