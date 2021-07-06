from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import ShilengaeUserSerializer
from .models import ShilengaeUser
class LoggedInUserApiView(generics.GenericAPIView):
    serializer_class = ShilengaeUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        
        return Response(self.get_serializer(request.user).data)

class UpdateUserApiView(generics.UpdateAPIView):
    serializer_class = ShilengaeUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ShilengaeUser.objects.all()

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)