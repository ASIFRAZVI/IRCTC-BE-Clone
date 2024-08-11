from rest_framework import serializers
from apps.authentication_app.models.user_model import CustomUser

class auth_serializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields="__all__"

    def validate(self, data):
        password=data.get('password')
        if password and len(password) <8:
            raise serializers.ValidationError('Password must be at least 8 characters long')
        return data

class login_serializer(serializers.Serializer):
    email=serializers.CharField(max_length=200)
    password=serializers.CharField(max_length=200)