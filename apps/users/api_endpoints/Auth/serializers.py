import re

from rest_framework import serializers

from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'role', 'avatar', 'password')


class OtpSerializer(serializers.Serializer):
    phone_validator = RegexValidator("^[0-9]{9}$", "Invalid phone number", 400)
    phone_number = serializers.CharField(max_length=13, validators=[phone_validator])


class ConfirmOtpSerializer(serializers.Serializer):
    phone_validator = RegexValidator("^[0-9]{9}$", "Invalid phone number", 400)
    phone_number = serializers.CharField(max_length=13, validators=[phone_validator])
    code = serializers.CharField(max_length=6, validators=[MinLengthValidator(6), MaxLengthValidator(6)])

