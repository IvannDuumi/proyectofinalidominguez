
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True)  
    last_name = models.CharField(max_length=100, blank=True)   
    code = models.CharField(max_length=10, blank=True, default='default_code')  
=======
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
>>>>>>> a59227e5c5c30dd1ae5685e3d4ce921d8ce9bf8d

    def __str__(self):
        return f'{self.user.username} Profile'
