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
    
    def validate_name(self, value):

        invalid = Category.objects.filter(parent=self.initial_data['parent'], name=self.initial_data['name']).exists()
        if invalid:
            raise serializers.ValidationError(f"There is already a category named {self.initial_data['name']} attached to the parent.")

        return value
    
