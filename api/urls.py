from django.urls import path

from api.views import UserProfileList, UserPostList

urlpatterns = [
    path('user_profile/', UserProfileList.as_view(), name='user_profile_list'),
    path('user_profile/<int:pk>', UserPostList.as_view(), name='user_post_list')
]
