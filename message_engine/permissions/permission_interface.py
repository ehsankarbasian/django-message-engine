from abc import ABC

from models import *


class PermissionInterface(ABC):
    
    def has_permission(user):
        pass
