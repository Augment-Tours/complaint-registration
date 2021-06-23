from rest_framework import generics, permissions, status

class TestView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        data = {
            'test': 'abcd'
        }

        return Response(data, status=status.HTTP_200_OK)