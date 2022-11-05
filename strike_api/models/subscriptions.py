from __future__ import annotations

from typing import List

from strike_api.models.generic import StrikeAPIModel


class Subscription(StrikeAPIModel):
    id: str
    webhook_url: str
    webhook_version: str
    enabled: bool
    created: str
    event_types: List[str]


class Subscriptions(StrikeAPIModel):
    __root__: List[Subscription]
