
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from registrants.views import Testing, register,view_profile, Home, AllUsers, update_profile, RandomUser, MaleUser, FemaleUser, add_post, login_view_profile, NonBinaryUser


urlpatterns = [
    path('register/', register, name='sign-up-page'),
    path('test/', Testing.as_view(), name='test-page'),
    path('user_profile/', login_view_profile, name='view-profile-page'),
    path('user_profile/<int:pk>', view_profile, name='view-profile-page-pk'),
    path('', register, name='home-page'),
    path('all_users/', AllUsers.as_view(), name='all-users-page'), 
    path('user_profile/edit', update_profile, name='profile-update-page'),
    path('random_user/', RandomUser.as_view(), name='random-user-page'),
    path('male_user/', MaleUser.as_view(), name='male-user-page'),
    path('female_user/', FemaleUser.as_view(), name='female-user-page'),
    path('non_binary_user/', NonBinaryUser.as_view(), name='non-binary-user-page'),
    path('post/', add_post, name='user-post-page'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)