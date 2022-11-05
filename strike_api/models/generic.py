from __future__ import annotations
import humps
import re

from pydantic import BaseModel


def to_snake_case(name: str) -> str:
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub("__([A-Z])", r"_\1", name)
    name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name)
    return name.lower()


class StrikeAPIModel(BaseModel):
    class Config:
        alias_generator = humps.camelize


class ItemsResponse(StrikeAPIModel):
    items: StrikeAPIModel
    count: int
