from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.response import Response

from .serializers import ShilengaeUserProfileSerializer, ShilengaeUserSerializer
from .models import ShilengaeUser, ShilengaeUserProfile

class LoggedInUserApiView(generics.GenericAPIView):
    serializer_class = ShilengaeUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        
        return Response(self.get_serializer(request.user).data)

class GetUserProfileApiView(generics.GenericAPIView):
    serializer_class = ShilengaeUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = ShilengaeUser.objects.get(pk=user_id)
        return Response(self.get_serializer(user).data)

class UpdateUserProfileApiView(generics.GenericAPIView):
    serializer_class = ShilengaeUserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = ShilengaeUser.objects.get(pk=user_id)
        user_profile = ShilengaeUserProfile.objects.get(user=user)
        serializer = self.get_serializer(user_profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UpdateUserApiView(generics.UpdateAPIView):
    serializer_class = ShilengaeUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ShilengaeUser.objects.all()

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ListUsersApiView(generics.ListAPIView):
    serializer_class = ShilengaeUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ShilengaeUser.objects.all()


class SearchUserApiView(generics.ListAPIView):
    serializer_class = ShilengaeUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        search_term = self.request.query_params.get('search_term', '')
        return ShilengaeUser.objects.filter(Q(username__icontains=search_term) |
                                            Q(first_name__icontains=search_term) |
                                            Q(last_name__icontains=search_term))