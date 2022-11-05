from __future__ import annotations

from strike_api.models.generic import StrikeAPIModel


class TargetAmount(StrikeAPIModel):
    currency: str
    amount: str


class SourceAmount(StrikeAPIModel):
    currency: str
    amount: str


class ConversionRate(StrikeAPIModel):
    amount: str
    source_currency: str
    target_currency: str


class Quote(StrikeAPIModel):
    quote_id: str
    description: str
    ln_invoice: str
    onchain_address: str
    expiration: str
    expiration_in_sec: int
    target_amount: TargetAmount
    source_amount: SourceAmount
    conversion_rate: ConversionRate
