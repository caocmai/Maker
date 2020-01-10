from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from registrants.models import UserProfile, UserPost
from api.serializers import UserProfileSerializer
from api.serializers import UserPostSerializer


class UserProfileList(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserPostList(RetrieveDestroyAPIView):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer