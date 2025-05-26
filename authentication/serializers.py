from rest_framework import serializers
from .models import User
from teams.models import Team
from django.contrib.auth import authenticate

class TeamMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    team = TeamMinimalSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'email', 'role', 'team', 'createdAt', 'updatedAt']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'email', 'password', 'role', 'team']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        data['user'] = user
        return data