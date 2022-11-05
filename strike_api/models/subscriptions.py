from __future__ import annotations

from typing import List

from strike_api.models.generic import StrikeAPIModel


class Subscription(StrikeAPIModel):
    id: str
    webhookUrl: str
    webhookVersion: str
    enabled: bool
    created: str
    eventTypes: List[str]


class Subscriptions(StrikeAPIModel):
    __root__: List[Subscription]
