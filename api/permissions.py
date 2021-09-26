from rest_framework import permissions

from users.models import CRUser

class ModeratorPermissions(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.type == CRUser.TYPE.MODERATOR and super().has_permission(request, view)

class FeedbackUpdatePermissions(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
