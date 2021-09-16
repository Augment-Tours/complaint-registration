# Create a serializer
from rest_framework import serializers
from rest_framework.fields import CreateOnlyDefault

from .models import Feedback
from users.models import CRUser


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=CRUser.objects.all(),
        required=True,
    )

    class Meta:
        model = Feedback
        fields = ['id',  'subject', 'file', 'feedback', 'user', 'created_at', 'updated_at']