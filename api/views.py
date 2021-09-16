from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import serializers

from .serializers import FeedbackSerializer
from .models import Feedback

class ListOwnedFeedbackApiView(generics.ListAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]
    

    def get_queryset(self):
        # get logged in users feedbacks
        return Feedback.objects.filter(user=self.request.user)

class CreateFeedbackApiView(generics.CreateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateFeedbackApiView(generics.UpdateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Feedback.objects.all()

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)