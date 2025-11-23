from permission_interface import PermissionInterface as _PermissionInterface


class AllowAny(_PermissionInterface):

    def has_permission(user):
        return True


class AllowNobody(_PermissionInterface):

    def has_permission(user):
        return False


class Verified(_PermissionInterface):

    def has_permission(user):
        return


class NotVerified(_PermissionInterface):

    def has_permission(user):
        return
