from rest_framework import generics
from .serializers import TranslationPackSerializer
from .models import TranslationPack

# Create your views here.
class CreateTranslationPackApiView(generics.CreateAPIView):
    serializer_class = TranslationPackSerializer

class ListAllTranslationPacks(generics.ListAPIView):
    serializer_class = TranslationPackSerializer
    queryset = TranslationPack.objects.all()