from django.contrib import admin
from .models import UserProfile, UserPost

admin.site.register(UserProfile)
admin.site.register(UserPost)