from django.urls import path
from registrants.views import SignUpView

urlpatterns = [
    path('', SignUpView.as_view(), name="sign-up-page"),

]
