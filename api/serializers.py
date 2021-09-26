# Create a serializer
from rest_framework import serializers
from rest_framework.fields import CreateOnlyDefault

from .models import Feedback
from users.models import CRUser


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=CRUser.objects.all(),
        required=False,
    )
    username = serializers.SerializerMethodField()

    class Meta:
        model = Feedback
        fields = ['id',  'subject', 'file', 'feedback',
                  'user', 'username', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def get_username(self, obj):
        return obj.user.username