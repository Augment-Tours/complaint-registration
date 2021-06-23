from rest_framework import generics, permissions, status
from rest_framework.response import Response

class TestView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        data = {
            'test': 'abcd'
        }

        return Response(data, status=status.HTTP_200_OK)