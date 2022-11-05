from __future__ import annotations

import pytest
from strike_api.events import Event

from strike_api.events import get_event, get_events
from requests.exceptions import HTTPError


@pytest.fixture(scope="module")
def vcr_config():
    return {"filter_headers": ["Authorization"]}


@pytest.mark.vcr
def test_get_events():
    events = get_events()

    assert isinstance(events.items, list)
    assert isinstance(events.count, int)


@pytest.mark.vcr
def test_get_event_not_found():
    event_id = "fb0c113e-dc9a-45c5-a491-1b036bc8ac7a"
    with pytest.raises(HTTPError) as excinfo:
        get_event(event_id)
    assert "404 Client Error" in str(excinfo.value)


@pytest.mark.vcr
def test_get_event():
    event_id = "1552121f-ce10-4f15-894f-332516afd3cb"
    event = get_event(event_id)

    assert isinstance(event, Event)
    assert event.eventType == "invoice.created"
