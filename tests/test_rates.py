from __future__ import annotations


def test_get_ticker():
    assert isinstance(get_ticker(), dict)