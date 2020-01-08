
from django.urls import path
from registrants.views import Testing, register


urlpatterns = [
    path('', register, name="sign-up-page"),
    path('test/', Testing.as_view(), name="test-page")

]
