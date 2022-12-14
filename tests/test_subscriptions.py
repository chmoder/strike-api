from __future__ import annotations

import pytest

from strike_api.subscriptions import (
    create_subscription,
    delete_subscription,
    get_subscription,
    get_subscriptions,
    update_subscription,
)


@pytest.fixture(scope="module")
def vcr_config():
    return {"filter_headers": ["Authorization"]}


@pytest.mark.vcr
def test_get_subscriptions():
    subscriptions = get_subscriptions()
    count = len([i for i in subscriptions])
    assert isinstance(count, int)


@pytest.mark.vcr
def test_get_subscription():
    subscription = get_subscription("9a2deb94-485a-4643-8d84-6a5058899567")
    assert isinstance(subscription.event_types, list)


@pytest.mark.vcr
def test_create_subscription():
    subscription = create_subscription(
        "https://www.chmoder.org/hook",
        "v1",
        "fake_secret",
        True,
        ["invoice.created", "invoice.updated"],
    )

    assert isinstance(subscription.event_types, list)


@pytest.mark.vcr
def test_update_subscription():
    subscription = update_subscription(
        "ef44e311-ec59-467b-8ddf-38784edda1c1",
        "https://www.chmoder.org/hook2",
        "v1",
        "fake_secret",
        True,
        ["invoice.created", "invoice.updated"],
    )

    assert isinstance(subscription.event_types, list)


@pytest.mark.vcr
def test_delete_subscription():
    response = delete_subscription("b9cc81c3-8097-419c-a7d0-1ed5f1abfd28")
    assert response is None
