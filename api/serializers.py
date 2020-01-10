from rest_framework.serializers import ModelSerializer
from registrants.models import UserProfile, UserPost


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserPostSerializer(ModelSerializer):
    class Meta:
        model = UserPost
        fields = '__all__'