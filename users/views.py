from rest_framework import generics, permissions
from rest_framework.response import Response

from api.permissions import ModeratorPermissions

from .serializers import CRUserSerializer
from .models import CRUser

class ListUsersApiView(generics.ListAPIView):
    serializer_class = CRUserSerializer
    permission_classes = [ModeratorPermissions]
    queryset = CRUser.objects.all()

class ToggleUserStatusApiView(generics.GenericAPIView):
    serializer_class = CRUserSerializer
    permission_classes = [ModeratorPermissions]
    queryset = CRUser.objects.all()

    def post(self, request, *args, **kwargs):
        user: CRUser = self.get_object()
        user.toggle()
        return Response(self.get_serializer(user).data)