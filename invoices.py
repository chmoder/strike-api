import json
import typing

from base import call_api


def get_invoices(
    filter: str = None, orderby: str = None, skip: int = None, top: int = None
):
    url = "https://api.strike.me/v1/invoices"

    payload = {}

    return call_api("GET", url, data=payload)


def get_invoice(invoice_id: str) -> dict:
    url = f"https://api.strike.me/v1/invoices/{invoice_id}"

    return call_api("GET", url)


def issue_invoice(
    handle: typing.Optional[str] = None,
    correlation_id: str = None,
    description: str = None,
    currency: str = None,
    amount: str = None,
) -> dict:
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

    return call_api("POST", url, headers=headers, data=payload)


def issue_quote(invoice_id: str) -> dict:
    url = f"https://api.strike.me/v1/invoices/{invoice_id}/quote"

    headers = {"Content-Length": "0"}

    return call_api("POST", url, headers=headers)


def cancel_invoice(invoice_id: str) -> dict:
    url = f"https://api.strike.me/v1/invoices/{invoice_id}/cancel"

    return call_api("PATCH", url)
