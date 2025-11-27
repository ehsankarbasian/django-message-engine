from typing import List, TypeVar, Dict


ItemClass = TypeVar('item_class')


class BaseRegistry:
    
    _REGISTRY: Dict[str, ItemClass] = None
    
    @classmethod
    def register(cls, name: str, item_class: ItemClass):
        if name not in cls._REGISTRY:
            cls._REGISTRY[name] = item_class
    
    @classmethod
    def get(cls, name: str):
        return cls._REGISTRY.get(name, None)
    
    @classmethod
    def exists(cls, name: str) -> bool:
        return name in cls._REGISTRY
    
    @classmethod
    def list_names(cls) -> List[str]:
        return list(cls._REGISTRY.keys())
    
    @classmethod
    def list_classes(cls) -> List[ItemClass]:
        return list(cls._REGISTRY.values())
    
    @classmethod
    def _clear(cls):
        cls._REGISTRY.clear()
