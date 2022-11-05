import json
import typing

from strike_api.base import call_api
from strike_api.models.invoices import Invoice, InvoiceItems
from strike_api.models.quotes import Quote


def get_invoices(
    filter_: typing.Optional[str] = None,
    orderby: typing.Optional[str] = None,
    skip: typing.Optional[int] = None,
    top: typing.Optional[int] = None,
) -> InvoiceItems:
    """Get Invoices
    Required scopes: partner.webhooks.manage
    OData filtering syntax can be seen `here <https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-odata/7d6c4117-317d-4860-915b-7e321be017e3>`_.  Ordering syntax can be seen `here <https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-odata/793b1e83-95ee-4446-8434-f5b634f20d1e>`_.

    Args:
        filter_ (str, optional): Filter the results using OData syntax. Supported properties: invoiceId, created, currency, state, issuerId, receiverId, payerId, correlationId. Defaults to None.
        orderby (str, optional): Order the results using OData syntax. Supported properties: created. Defaults to None.
        skip (int, optional): Skip the specified number of entries. Defaults to None.
        top (int, optional): Get the top X number of records. Default value: 50. Max value: 100. Defaults to None.

    Returns:
       dict: invoices
    """
    url = "https://api.strike.me/v1/invoices"

    payload = {"filter": filter_, "orderby": orderby, "skip": skip, "top": top}

    response = call_api("GET", url, params=payload)
    return InvoiceItems.parse_obj(response)


def get_invoice(invoice_id: str) -> Invoice:
    """get invoice by id

    Args:
        invoice_id (str): Invoice id

    Returns:
        dict: invoice
    """
    url = f"https://api.strike.me/v1/invoices/{invoice_id}"

    response = call_api("GET", url)
    return Invoice.parse_obj(response)


def issue_invoice(
    handle: typing.Optional[str] = None,
    correlation_id: typing.Optional[str] = None,
    description: typing.Optional[str] = None,
    currency: typing.Optional[str] = None,
    amount: typing.Optional[str] = None,
) -> Invoice:
    """Issue a new invoice

    Only currencies which are invoiceable for the caller's account can be used. Invoiceable currencies can be found using get account profile endpoint.

    Args:
        handle (typing.Optional[str], optional): handle, if specifying a receiver. Defaults to None.
        correlation_id (str, optional): Invoice correlation id. Must be a unique value. Can be used to correlate the invoice with an external entity. Defaults to None.
        description (str, optional): Invoice description. Defaults to None.
        currency (str, optional): Currency code [BTC, USD, EUR, USDT, GBP]. Defaults to None.
        amount (str, optional): Currency amount in decimal format. Defaults to None.

    Returns:
        dict: invoice
    """
    if handle:
        url = f"https://api.strike.me/v1/invoices/handle/{handle}"
    else:
        url = "https://api.strike.me/v1/invoices"

    payload = json.dumps(
        {
            "correlationId": correlation_id,
            "description": description,
            "amount": {"currency": currency, "amount": amount},
        }
    )

    headers = {"Content-Type": "application/json"}

    response = call_api("POST", url, headers=headers, data=payload)
    return Invoice.parse_obj(response)


def issue_quote(invoice_id: str) -> Quote:
    """Issue a new quote for specified invoice

    Args:
        invoice_id (str): Id of invoice for which the quote is requested

    Returns:
        dict: quote
    """
    url = f"https://api.strike.me/v1/invoices/{invoice_id}/quote"

    headers = {"Content-Length": "0"}

    response = call_api("POST", url, headers=headers)
    return Quote.parse_obj(response)


def cancel_invoice(invoice_id: str) -> Invoice:
    """Cancel an unpaid invoice

    Args:
        invoice_id (str): Id of invoice for which the cancellation is requested

    Returns:
        dict: invoice
    """
    url = f"https://api.strike.me/v1/invoices/{invoice_id}/cancel"

    response = call_api("PATCH", url)
    return Invoice.parse_obj(response)
