from rest_framework import serializers

from .models import Category, Form, FormField
from api.enums import STATUS


class FormFieldSerializer(serializers.ModelSerializer):
    form = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    class Meta:
        model = FormField
        fields = ['id', 'type', 'description', 'hint', 'label', 'position', 'is_required', 'form', 'data', 'created_at']
    
    def create(self, validated_data):
        form_field: FormField = super().create(validated_data)
        form_field.form = validated_data.get('form')
        form_field.save()

        return form_field
class FormSerializer(serializers.ModelSerializer):
    form_fields = FormFieldSerializer(many=True, required=False)
    form_fields_count = serializers.SerializerMethodField()
    class Meta:
        model = Form
        fields = ['id', 'name', 'form_fields', 'form_fields_count', 'created_at']
    
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

    def validate_form_fields(self, value):
        positions = set()
        for field in value:
            if field.get('position') in positions:
                raise serializers.ValidationError('Fields must have unique positions.')
            positions.add(field.get('position'))
        return value
class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False, allow_null=True)
    form = FormSerializer
    parent_category_name = serializers.SerializerMethodField()
    form_name = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent', 'form', 'level',
                    'parent_category_name', 'form_name', 'status', 
                    'created_at', 'updated_at']

    
    def create(self, validated_data):
        category: Category = super().create(validated_data)
        category.add_self_to_parent()
        category.form = validated_data.get('form', None)
        category.parent = validated_data.get('parent')
        if category.parent:
            category.level = category.parent.level + 1

        category.save()

        return category
    
    def update(self, instance: Category, validated_data):
    #    instance.add_self_to_parent()
        instance.parent = validated_data.get('parent', instance.parent)
        instance.name = validated_data.get('name', instance.name)
        instance.form = validated_data.get('form', instance.form)
        instance.save()
        instance.add_self_to_parent()
        return instance
    
    def validate_name(self, value):

        invalid = Category.objects.filter(parent=self.initial_data.get('parent', None), name=self.initial_data.get('name', None)).exists()
        if self.instance and self.instance.name == value:
            return value
        if invalid:
            raise serializers.ValidationError(f"There is already a category named {self.initial_data['name']} attached to the parent.")

        return value

    def get_parent_category_name(self, category):
        if category.parent:
            return category.parent.name
    
    def get_form_name(self, category):
        if category.form:
            return category.form.name