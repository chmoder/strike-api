from __future__ import annotations
import humps
import typing

from pydantic import BaseModel


class StrikeAPIModel(BaseModel):
    class Config:
        alias_generator = humps.camelize  # type: ignore


class ItemsResponse(StrikeAPIModel):
    items: typing.List[typing.Any]
    count: int
