from __future__ import annotations

from typing import List

from strike_api.models.generic import StrikeAPIModel


class Currency(StrikeAPIModel):
    currency: str
    isDefaultCurrency: bool
    isAvailable: bool
    isInvoiceable: bool


class Account(StrikeAPIModel):
    handle: str
    avatarUrl: str
    canReceive: bool
    currencies: List[Currency]
