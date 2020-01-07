from django.urls import path, include
# from users.views import

urlpatterns = [
    path('', Home.as_view(), name='home-page'),


]
