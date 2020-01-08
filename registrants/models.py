from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    location = models.CharField(max_length=30)
    age = models.IntegerField()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Non-Binary')
    )
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    def __str__(self):
        return self.user.username