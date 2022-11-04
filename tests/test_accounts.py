from __future__ import annotations

import pytest
from strike_api.accounts import get_account


@pytest.fixture(scope="module")
def vcr_config():
    return {"filter_headers": ["Authorization"]}


# @pytest.mark.vcr
# def test_get_account_by_id():
#     assert isinstance(get_account(account_id="953680ce-2149-4ce2-a5e3-82bb9a57be41"), list)


@pytest.mark.vcr
def test_get_account_by_handle():
    account = get_account(handle="chmoder")
    assert isinstance(account, dict)


@pytest.mark.vcr
def test_get_account_by_neither():
    with pytest.raises(ValueError) as excinfo:
        get_account()
    assert "use either account_id or handle" in str(excinfo.value)
