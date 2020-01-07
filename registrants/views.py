from django.shortcuts import render
from registrants.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    # success_url = reverse_lazy('registrationlogin')
    success_url = "test/"
    template_name = "registration/signup.html"

# Create your views here.

class Testing(CreateView):
    def get(self, request):
        return render(request, "registration/test.html", {"test": "test"})
