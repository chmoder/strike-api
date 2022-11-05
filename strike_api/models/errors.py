from __future__ import annotations

from strike_api.models.generic import StrikeAPIModel


class Data(StrikeAPIModel):
    status: int
    code: str
    message: str


class Error404(StrikeAPIModel):
    traceId: str
    data: Data


class Error401(StrikeAPIModel):
    data: Data
