from __future__ import annotations
import uuid

import pytest

from strike_api.invoices import (
    cancel_invoice,
    get_invoice,
    get_invoices,
    issue_invoice,
    issue_quote,
)


@pytest.fixture(scope="module")
def vcr_config():
    return {"filter_headers": ["Authorization"]}


@pytest.mark.vcr
def test_get_invoices():
    response = get_invoices()
    invoice_list = response["items"]
    count = response["count"]

    assert isinstance(response, dict)
    assert isinstance(invoice_list, list)
    assert isinstance(count, int)


@pytest.mark.vcr
def test_get_invoice_not_found():
    invoice_id = "fb0c113e-dc9a-45c5-a491-1b036bc8ac7a"
    response = get_invoice(invoice_id)
    data = response["data"]
    status = data["status"]

    assert isinstance(response, dict)
    assert isinstance(data, dict)
    assert status == 404


@pytest.mark.vcr
def test_issue_invoice():
    correltion_id = str(uuid.uuid4())
    description = "Invoice for order 123"
    currency = "USD"
    amount = "1.00"

    response = issue_invoice(
        correlation_id=correltion_id,
        description=description,
        currency=currency,
        amount=amount,
    )

    assert "state" in response
    invoice_state = response["state"]
    assert invoice_state == "UNPAID"


@pytest.mark.vcr
def test_issue_invoice_for_handle():
    handle = "chmoder"
    correltion_id = str(uuid.uuid4())
    description = "Invoice for order 123"
    currency = "USD"
    amount = "1.00"

    response = issue_invoice(
        handle=handle,
        correlation_id=correltion_id,
        description=description,
        currency=currency,
        amount=amount,
    )

    assert "state" in response
    invoice_state = response["state"]
    assert invoice_state == "UNPAID"


@pytest.mark.vcr
def test_cancel_invoice_not_found():
    invoice_id = "168722cd-8f0a-4a1e-8241-e79a7b9722be"

    response = cancel_invoice(invoice_id)

    data = response["data"]
    status = data["status"]

    assert isinstance(response, dict)
    assert isinstance(data, dict)
    assert status == 404


@pytest.mark.vcr
def test_issue_quote():
    invoice_id = "5f8a40b4-910f-439d-9a61-81fae87f0a8e"

    response = issue_quote(invoice_id)

    assert "quoteId" in response
    quote_id = response["quoteId"]
    assert len(quote_id) > 0
