
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from registrants.views import Testing, register,view_profile, Home, AllUsers, update_profile


urlpatterns = [
    path('register/', register, name='sign-up-page'),
    path('test/', Testing.as_view(), name='test-page'),
    path('user_profile/', view_profile, name='view-profile-page'),
    path('user_profile/<int:pk>', view_profile, name='view-profile-page-pk'),
    path('', Home.as_view(), name='home-page'),
    path('all_users/', AllUsers.as_view(), name='all-users-page'), 
    path('user_profile/edit', update_profile, name='profile-update-page'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)