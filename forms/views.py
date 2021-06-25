from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Form, FormField, FormFieldResponse

class TestView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):

        return Response(data, status=status.HTTP_200_OK)