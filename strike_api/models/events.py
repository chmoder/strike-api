from __future__ import annotations
import typing


from strike_api.models.generic import ItemsResponse, StrikeAPIModel


class Data(StrikeAPIModel):
    entityId: str


class Event(StrikeAPIModel):
    id: str
    eventType: str
    webhookVersion: str
    data: Data
    created: str
    deliverySuccess: bool


class Events(StrikeAPIModel):
    __root__: typing.List[Event]

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, index):
        return self.__root__[index]


class EventItems(ItemsResponse):
    items: typing.List[Event]
