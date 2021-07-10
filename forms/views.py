from django.db.models import Q
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import CategorySerializer
from .models import Category
class TestView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        data = {
            'abcd': 'test'
        }
        return Response(data, status=status.HTTP_200_OK)


class CreateCategoryApiView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class UpdateCategoryApiView(generics.UpdateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class SearchCategoryApiView(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        search_term = self.request.query_params.get('search_term')
        return Category.objects.filter(Q(name__icontains=search_term))
