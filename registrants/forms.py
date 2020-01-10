from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile, UserPost


class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(required=True, label="First Name")
    last_name = forms.CharField(required=True, label="Last Name")
    # age = forms.IntegerField(required=True, label="Age")
    # location = forms.CharField(required=True, label="Location")
    # picture = forms.FileField(label="Upload Image")

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()
        return user
  

class UserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ("location", "age", "image", "gender")
        widgets = {'gender': forms.RadioSelect}


class PostForm(forms.ModelForm):

    class Meta:
        model = UserPost
        fields = ("content", )