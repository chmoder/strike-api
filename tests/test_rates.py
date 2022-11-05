from __future__ import annotations

import pytest
from strike_api.rates import get_ticker


@pytest.fixture(scope="module")
def vcr_config():
    return {"filter_headers": ["Authorization"]}


@pytest.mark.vcr
def test_get_ticker():
    rates = get_ticker()
    count = len([i for i in rates])
    assert isinstance(count, int)
    assert float(rates[0].amount) > 0
