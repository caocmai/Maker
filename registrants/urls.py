from django.urls import path
from registrants.views import SignUpView, Testing

urlpatterns = [
    path('', SignUpView.as_view(), name="sign-up-page"),
    path('test/', Testing.as_view(), name="test-page")

]
