from __future__ import annotations

from abc import ABCMeta

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .base_registry import BaseRegistry


class AutoRegisterMeta(ABCMeta):
    # Must be verridden in each interface
    # _REGISTRY: BaseRegistry
    _ABSTRACT: bool

    def __new__(mcls, name, bases, attrs):
        cls = super().__new__(mcls, name, bases, attrs)

        if not attrs.get("_ABSTRACT", False):
            if cls._REGISTRY:
                cls._REGISTRY.register(name, cls)

        return cls
