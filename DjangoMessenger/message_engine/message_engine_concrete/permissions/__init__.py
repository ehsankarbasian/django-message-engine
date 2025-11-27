from message_engine.core.interfaces import PermissionInterface

from message_engine.models import MessageEndpoint


class AllowAny(PermissionInterface):
    _ABSTRACT = False

    @staticmethod
    def has_permission(user):
        return True


class AllowNobody(PermissionInterface):
    _ABSTRACT = False

    @staticmethod
    def has_permission(user):
        return False


class Verified(PermissionInterface):
    _ABSTRACT = False

    @staticmethod
    def has_permission(user):
        return MessageEndpoint.objects.filter(
            user=user,
            verified=True,
            is_active=True,
        ).exists()


class NotVerified(PermissionInterface):
    _ABSTRACT = False

    @staticmethod
    def has_permission(user):
        return not Verified.has_permission(user)
