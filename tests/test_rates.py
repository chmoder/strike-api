from __future__ import annotations

from strike_api.rates import get_ticker

def test_get_ticker():
    assert isinstance(get_ticker(), list)