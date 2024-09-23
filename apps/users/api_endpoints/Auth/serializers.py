import re

from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'role', 'avatar', 'password')


class OtpSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)

    def validate_phone_number(self,value):
        pattern = r'^[0-9]{9}$'

        if not re.match(pattern, value):
            raise serializers.ValidationError('Invalid phone number')

        return value


class ConfirmOtpSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)
    code = serializers.CharField(max_length=6)

    def validate_phone_number(self,value):
        pattern = r'^[0-9]{9}$'

        if not re.match(pattern, value):
            raise serializers.ValidationError('Invalid phone number')

        return value
