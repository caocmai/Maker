from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(required=True, label="First Name")
    last_name = forms.CharField(required=True, label="Last Name")
    age = forms.IntegerField(required=True, label="Age")
    location = forms.CharField(required=True, label="Location")
    picture = forms.ImageField()


    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "age", "location", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.age = self.cleaned_data["age"]
        user.location = self.cleaned_data["location"]
        if commit:
            user.save()
        return user
  
