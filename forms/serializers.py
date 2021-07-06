from rest_framework import serializers

from .models import Category
from api.enums import STATUS

class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False)
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent', 'created_at', 'updated_at']

    
    def save(self):
        category = super().save()

        if category.parent:
            category.ancestors.set(category.parent.ancestors.all()) 
            category.ancestors.add(category.parent)

            for ancestor in category.ancestors.all():
                ancestor.descendants.add(category)


        return category