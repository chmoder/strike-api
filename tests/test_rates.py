from __future__ import annotations

from strike_api import get_ticker

def test_get_ticker():
    assert isinstance(get_ticker(), dict)