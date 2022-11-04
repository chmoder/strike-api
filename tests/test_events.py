from __future__ import annotations

import pytest

from strike_api.events import get_event, get_events


@pytest.fixture(scope="module")
def vcr_config():
    return {"filter_headers": ["Authorization"]}


@pytest.mark.vcr
def test_get_events():
    response = get_events()
    event_list = response["items"]
    count = response["count"]

    assert isinstance(response, dict)
    assert isinstance(event_list, list)
    assert isinstance(count, int)


@pytest.mark.vcr
def test_get_event_not_found():
    event_id = "fb0c113e-dc9a-45c5-a491-1b036bc8ac7a"
    response = get_event(event_id)
    data = response["data"]
    status = data["status"]

    assert isinstance(response, dict)
    assert isinstance(data, dict)
    assert status == 404
