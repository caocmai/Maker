from django.shortcuts import render, redirect, get_object_or_404
from registrants.forms import ExtendedUserCreationForm, UserProfileForm, PostForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.models import User
from registrants.models import UserProfile, UserPost
from django.contrib.auth import authenticate, login


# When have time look at Corey's tutorial on this for creating user profile
# Since user is model is extended need two forms (form and profile_form)
def register(request):
    if request.method == 'POST':
        user_form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            
            messages.success(request, f'Account created for {username}!')

            return redirect('all-users-page')
    
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


class Testing(CreateView):
    def get(self, request):
        return render(request, 'registration/test.html', {'test': 'test'})


class Home(CreateView):
    
    def get(self, request):
        return render(request, 'base.html', {'test': 'test'})


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
            messages.success(request, ('Your profile was successfully updated!'))
            
            # This is to get the username and password so you can log a user in after they update their profile
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('view-profile-page')
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

    model = User

    def get(self, request):
        male_users = self.get_queryset().filter(userprofile__gender="M") # double underscore gender becuase extended model of User called userprofile
        return render(request, 'registrants/filtered_users.html', {'users': male_users})

class FemaleUser(CreateView):

    def get(self, request):
        female_users = User.objects.filter(userprofile__gender="F")  # __ because it's an extended model to the User, so need it
        return render(request, 'registrants/filtered_users.html', {'users': female_users})

class NonBinaryUser(CreateView):

    def get(self, request):
        non_binary_users = User.objects.filter(userprofile__gender="N")  # __ because it's an extended model to the User, so need it
        return render(request, 'registrants/filtered_users.html', {'users': non_binary_users})


def add_post(request):
    """User can add postings"""
    form = PostForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
          comment = form.save(commit=False)
          # Need to do this for all models.ForeignKey!!!!!
          comment.from_user = request.user
          comment.save()
          return redirect('view-profile-page')
    else:
        form = PostForm()
    return render(request, 'registrants/user_post.html', {'form': form})

def login_view_profile(request):
    user = request.user
    args = {'user': user}
    return render(request, 'registrants/login_user_profile.html', args)