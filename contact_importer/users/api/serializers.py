from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_email(self, attrs):
        if User.objects.filter(username=attrs).exists():
            raise serializers.ValidationError("This email is already registered")
        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data.get('email'), **validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class UserReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]
        read_only_fields = fields
