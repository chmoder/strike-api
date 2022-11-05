from __future__ import annotations
import humps

from pydantic import BaseModel


class StrikeAPIModel(BaseModel):
    class Config:
        alias_generator = humps.camelize


class ItemsResponse(StrikeAPIModel):
    items: StrikeAPIModel
    count: int
