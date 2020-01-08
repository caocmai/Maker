from django.shortcuts import render, redirect
from registrants.forms import ExtendedUserCreationForm, UserProfileForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login



# class SignUpView(SuccessMessageMixin, CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('test-page')
#     # success_url = "test/"
#     template_name = "registration/signup.html"
#     success_message = "An account was created successfully"


def register(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('test-page')
    
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form' : form, 'profile_form' : profile_form}
    return render(request, "registration/signup.html", context)


# Create your views here.

class Testing(CreateView):
    def get(self, request):
        return render(request, "registration/test.html", {"test": "test"})
