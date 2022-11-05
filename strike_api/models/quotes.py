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
    sourceCurrency: str
    targetCurrency: str


class Quote(StrikeAPIModel):
    quoteId: str
    description: str
    lnInvoice: str
    onchainAddress: str
    expiration: str
    expirationInSec: int
    targetAmount: TargetAmount
    sourceAmount: SourceAmount
    conversionRate: ConversionRate
