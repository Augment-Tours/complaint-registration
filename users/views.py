from rest_framework import generics, permissions
from rest_framework.response import Response

from .serializers import ShilengaeUserSerializer

class LoggedInUserApiView(generics.GenericAPIView):
    serializer_class = ShilengaeUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        
        return Response(self.get_serializer(request.user).data)

class SignupUserApiView(generics.CreateAPIView):
    serializer_class = ShilengaeUserSerializer