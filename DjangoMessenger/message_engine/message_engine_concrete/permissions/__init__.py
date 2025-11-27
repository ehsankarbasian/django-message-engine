from message_engine.core.interfaces.permission import PermissionInterface as _PermissionInterface


class AllowAny(_PermissionInterface):

    @staticmethod
    def has_permission(user):
        return True


class AllowNobody(_PermissionInterface):

    @staticmethod
    def has_permission(user):
        return False


class Verified(_PermissionInterface):

    @staticmethod
    def has_permission(user):
        return


class NotVerified(_PermissionInterface):

    @staticmethod
    def has_permission(user):
        return
