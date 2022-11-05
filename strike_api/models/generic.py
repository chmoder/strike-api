from __future__ import annotations
import re
import typing

from pydantic import BaseModel


def to_snake_case(name: str) -> str:
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub("__([A-Z])", r"_\1", name)
    name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name)
    return name.lower()


class StrikeAPIModel(BaseModel):
    pass
    # class Config:
    #     alias_generator = to_snake_case


class ItemsResponse(BaseModel):
    items: typing.List[typing.Any]
    count: int
