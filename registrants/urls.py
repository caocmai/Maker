from django.urls import path, include
from registrants.views import SignUpView

urlpatterns = [
    path('', SignUpView.as_view(), name="sign-up-page"),

]
