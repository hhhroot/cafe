from django.contrib.auth import get_user_model
from rest_framework import serializers

from cafes.serializers import CafeLikeSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    like_cafes = CafeLikeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "nickname",
            "image",
            "password",
            "like_cafes",
        ]
