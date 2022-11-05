from __future__ import annotations
from enum import Enum
import typing


from strike_api.models.generic import ItemsResponse, StrikeAPIModel


class INVOICE_STATES(Enum):
    UNPAID = "UNPAID"
    PENDING = "PENDING"
    PAID = "PAID"
    CANCELLED = "CANCELLED"


class Amount(StrikeAPIModel):
    currency: str
    amount: str


class Invoice(StrikeAPIModel):
    invoiceId: str
    amount: Amount
    state: str
    created: str
    correlation_id: str
    description: str
    issuer_id: str
    receiver_id: str


class Invoices(StrikeAPIModel):
    __root__: typing.List[Invoice]

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, index):
        return self.__root__[index]


class InvoiceItems(ItemsResponse):
    items: typing.List[Invoice]
