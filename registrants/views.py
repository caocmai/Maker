from django.shortcuts import render, redirect
from registrants.forms import ExtendedUserCreationForm, UserProfileForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.models import User
from registrants.models import UserProfile
from django.contrib.auth import authenticate, login



# class SignUpView(SuccessMessageMixin, CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('test-page')
#     # success_url = "test/"
#     template_name = "registration/signup.html"
#     success_message = "An account was created successfully"

# When have time look at Corey's tutorial on this for creating user profile
def register(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

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

            return redirect('home-page')
    
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


def update_profile(request):
    if request.method == 'POST':
        user_form = ExtendedUserCreationForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated! Please re-login to your new account!'))
            return redirect('all-users-page')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = ExtendedUserCreationForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'registrants/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


class RandomUser(CreateView):

    model = User

    def get(self, request):
        random_user = self.get_queryset().order_by('?')[0]
        return render(request, 'registrants/user_profile.html', {'user': random_user})

class MaleUser(CreateView):

    model = UserProfile

    def get(self, request):
        male_user = self.get_queryset().filter(gender='M')
        return render(request, 'registrants/male_users.html', {'users': male_user})

class FemaleUser(CreateView):

    def get(self, request):
        female_user = User.objects.filter(userprofile="10")
        return render(request, 'registrants/male_users.html', {'users': female_user})