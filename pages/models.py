from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
  
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=200, blank=True)
    
    code = models.CharField(max_length=50, unique=True)
   
    cover = models.ImageField(upload_to='pages/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
   
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
