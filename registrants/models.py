from django.db import models
from django.contrib.auth.models import User

# To access this, it's User.userprofile.whatever
class UserProfile(models.Model): # Now django will refer to this as userprofile
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    location = models.CharField(max_length=30, help_text='Enter the city')
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

class UserPost(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.PROTECT)
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
