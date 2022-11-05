from __future__ import annotations

import pytest
from strike_api.accounts import get_account
from strike_api.models.accounts import Account
from requests.exceptions import HTTPError


@pytest.fixture(scope="module")
def vcr_config():
    return {"filter_headers": ["Authorization"]}


@pytest.mark.vcr
def test_get_account_by_id_not_found():
    account_id = "953680ce-2149-4ce2-a5e3-82bb9a57be41"
    with pytest.raises(HTTPError) as excinfo:
        get_account(account_id)
    assert "404 Client Error" in str(excinfo.value)


@pytest.mark.vcr
def test_get_account_by_handle():
    account = get_account(handle="chmoder")
    assert isinstance(account, Account)
    assert account.handle == "chmoder"


@pytest.mark.vcr
def test_get_account_by_neither():
    with pytest.raises(ValueError) as excinfo:
        get_account()
    assert "use either account_id or handle" in str(excinfo.value)
