from rest_framework import serializers

from .models import Category, Form, FormField
from api.enums import STATUS


class FormFieldSerializer(serializers.ModelSerializer):
    form = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    class Meta:
        model = FormField
        fields = ['id', 'type', 'description', 'hint', 'label', 'position', 'form', 'data']
class FormSerializer(serializers.ModelSerializer):
    form_fields = FormFieldSerializer(many=True, required=False)
    form_fields_count = serializers.SerializerMethodField()
    class Meta:
        model = Form
        fields = ['id', 'name', 'form_fields', 'form_fields_count']
    
    def create(self, validated_data):
        fields_data = validated_data.pop('form_fields', [])
        form = Form.objects.create(**validated_data)
        self.add_fields_to_form(form, fields_data)
        return form
    
    def update(self, instance, validated_data):
        fields_data = validated_data.pop('form_fields', [])
        self.add_fields_to_form(instance, fields_data)
        return super().update(instance, validated_data)
    
    def add_fields_to_form(self, instance, fields_data):
        for field_data in fields_data:
            FormField.objects.create(form=instance, **field_data)
        
    def get_form_fields_count(self, obj):
        return obj.form_fields.count()

class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False)
    form = FormSerializer
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent', 'form', 'created_at', 'updated_at']

    
    def create(self, validated_data):
        category: Category = super().create(validated_data)
        category.add_self_to_parent()
        category.country = validated_data.get('country')
        category.save()

        return category
    
    def validate_name(self, value):

        invalid = Category.objects.filter(parent=self.initial_data.get('parent', None), name=self.initial_data.get('name', None)).exists()
        if invalid:
            raise serializers.ValidationError(f"There is already a category named {self.initial_data['name']} attached to the parent.")

        return value
