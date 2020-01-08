
from django.urls import path
from registrants.views import Testing, register,view_profile, Home, AllUsers, edit_profile


urlpatterns = [
    path('register/', register, name='sign-up-page'),
    path('test/', Testing.as_view(), name='test-page'),
    path('user_profile/', view_profile, name='view-profile-page'),
    path('user_profile/<int:pk>', view_profile, name='view-profile-page-pk'),
    path('', Home.as_view(), name='home-page'),
    path('all_users/', AllUsers.as_view(), name='all-users-page'), 
    path('user_profile/edit', edit_profile, name='profile-update-page'),
    # path('profile/edit/', edit_profile, name='edit_profile')

]
