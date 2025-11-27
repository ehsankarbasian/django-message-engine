from abc import ABCMeta


class AutoRegisterMeta(ABCMeta):
    # Must be verridden in each interface
    # _REGISTRY: BaseRegistry
    _ABSTRACT: bool

    def __new__(mcls, name, bases, attrs):
        cls = super().__new__(mcls, name, bases, attrs)

        if not attrs.get("_ABSTRACT", False):
            if hasattr(cls, '_REGISTRY'):
                cls._REGISTRY.register(name, cls)

        return cls
