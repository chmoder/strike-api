from src.rates import get_ticker


def test_get_ticker():
    assert isinstance(get_ticker(), dict)