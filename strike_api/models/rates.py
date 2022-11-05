from __future__ import annotations

from typing import List

from strike_api.models.generic import StrikeAPIModel


class Rate(StrikeAPIModel):
    amount: str
    source_currency: str
    target_currency: str


class Rates(StrikeAPIModel):
    __root__: List[Rate]

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, index):
        return self.__root__[index]
