from django.shortcuts import render, redirect
from registrants.forms import ExtendedUserCreationForm, UserProfileForm, EditProfileForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.models import User

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
            
            messages.success(request, f'Account created for {username}!')


            return redirect('test-page')
    
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form' : form, 'profile_form' : profile_form}
    return render(request, "registration/signup.html", context)



def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'registrants/user_profile.html', args)


# Create your views here.

class Testing(CreateView):
    def get(self, request):
        return render(request, "registration/test.html", {"test": "test"})

class Home(CreateView):
    
    def get(self, request):
        return render(request, "base.html", {"test": "test"})

class AllUsers(CreateView):

    model = User

    def get(self, request):
        users = self.get_queryset().all()
        return render(request, 'registrants/all_users.html', {'users': users})


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('view-profile-page'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registrants/edit_profile.html', args)