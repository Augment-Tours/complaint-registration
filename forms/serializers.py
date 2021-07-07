from rest_framework import serializers

from .models import Category
from api.enums import STATUS

class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False)
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent', 'created_at', 'updated_at']

    
    def save(self):
        category: Category = super().save()
        category.add_self_to_parent()

        return category