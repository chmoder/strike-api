from __future__ import annotations

import pytest
from strike_api.rates import get_ticker


@pytest.fixture(scope="module")
def vcr_config():
    return {"filter_headers": ["Authorization"]}


@pytest.mark.vcr
def test_get_ticker():
    assert isinstance(get_ticker(), list)
