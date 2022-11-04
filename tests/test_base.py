from __future__ import annotations
import os

import pytest

from strike_api.base import call_api


@pytest.fixture(scope="module")
def vcr_config():
    return {"filter_headers": ["Authorization"]}


@pytest.mark.vcr
def test_missing_strike_api_key():
    strike_api_key = os.environ.get("STRIKE_API_KEY")
    os.environ["STRIKE_API_KEY"] = ""

    with pytest.raises(EnvironmentError) as excinfo:
        call_api()
    assert "STRIKE_API_KEY not found" in str(excinfo.value)

    os.environ["STRIKE_API_KEY"] = strike_api_key
