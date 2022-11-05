from __future__ import annotations

from typing import List

from strike_api.models.generic import StrikeAPIModel


class Currency(StrikeAPIModel):
    currency: str
    is_default_currency: bool
    is_available: bool
    is_invoiceable: bool


class Account(StrikeAPIModel):
    handle: str
    avatar_url: str
    can_receive: bool
    currencies: List[Currency]
