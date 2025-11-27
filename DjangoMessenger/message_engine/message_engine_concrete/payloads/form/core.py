from typing import List

from message_engine.core.interfaces import AbstractPayloadItem
from .items import FormItemInterface


class BaseForm(AbstractPayloadItem):
    
    def __init__(self):
        self._items: List[FormItemInterface] = []

    @property
    def items(self):
        return self._items
    
    def add_item(self, item: FormItemInterface):
        self._items.append(item)
