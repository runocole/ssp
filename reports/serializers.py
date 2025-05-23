from rest_framework import serializers
from .models import Team, Report, ReportImage
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['email'],
            password=data['password']
        )
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        data['user'] = user
        return data 


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields = "__all__"

class ReportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReportImage
        fields = ["id", "image"]

class ReportSerializer(serializers.ModelSerializer):
    coach = UserSerializer(read_only=True)
    images = ReportImageSerializer(many=True, required=False, write_only=True)

    class Meta:
        model = Report
        fields = [
            "id", "coach", "team", "title", "in_possession",
            "out_of_possession", "pressing_systems", "created_at",
            "images", "stats_data"
        ]

    def create(self, validated_data):
        # Extract images data from validated_data
        images_data = self.context['request'].FILES.getlist('images')
        report = Report.objects.create(
            coach=self.context['request'].user,
            team=validated_data.get('team'),
            title=validated_data.get('title'),
            in_possession=validated_data.get('in_possession', ''),
            out_of_possession=validated_data.get('out_of_possession', ''),
            pressing_systems=validated_data.get('pressing_systems', ''),
            stats_data=validated_data.get('stats_data', '')
        )

        for image in images_data:
            ReportImage.objects.create(report=report, image=image)

        return report