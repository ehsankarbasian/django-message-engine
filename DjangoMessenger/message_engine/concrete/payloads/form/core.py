from typing import List

from message_engine.core.interfaces.payload import PayloadItemInterface
from .items import FormItemInterface


class BaseForm(PayloadItemInterface):
    
    def __init__(self):
        self._items: List[FormItemInterface] = []

    @property
    def items(self):
        return self._items
    
    def add_item(self, item: FormItemInterface):
        self._items.append(item)
