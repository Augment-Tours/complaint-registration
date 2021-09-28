from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import serializers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt

from .serializers import FeedbackSerializer
from .models import Feedback
from .permissions import ModeratorPermissions, FeedbackUpdatePermissions

from users.models import CRUser
from users.serializers import CRUserSerializer


class ListOwnedFeedbackApiView(generics.ListAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # get logged in users feedbacks
        return Feedback.objects.filter(user=self.request.user)


class ListAllFeedbackApiView(generics.ListAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [ModeratorPermissions]
    queryset = Feedback.objects.all()

# @method_decorator(csrf_protect, name='dispatch')
class CreateFeedbackApiView(generics.CreateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if request.data.get('file') and request.data.get('file').size > settings.MAX_UPLOAD_SIZE:
            return Response({'detail': ['* File size too large']}, status=400)
        return super().post(request, *args, **kwargs)


class UpdateFeedbackApiView(generics.UpdateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [FeedbackUpdatePermissions]
    queryset = Feedback.objects.all()

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ToggleMemberAccountStatus(generics.GenericAPIView):
    serializer_class = CRUserSerializer
    permission_classes = [ModeratorPermissions]

    def post(self, request, *args, **kwargs):
        user: CRUser = get_object_or_404(CRUser, pk=kwargs['pk'])

        # do not deactivate if user is also moderator
        if user.type == CRUser.TYPE.MODERATOR:
            return Response({"message": "You are not allowed to disable this user"}, status=403)

        user.toggle()

        return Response({"message": "User account disabled"}, status=200)


class ViewAllMembersFeedbacks(generics.GenericAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [ModeratorPermissions]

    def get(self, request, *args, **kwargs):
        feedbacks = Feedback.objects.all()
        serializer = self.get_serializer(feedbacks, many=True)
        return Response(serializer.data)

class LoggedInProfile(generics.GenericAPIView):
    serializer_class = CRUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        return Response({'success': 'CSRF cookie set'})