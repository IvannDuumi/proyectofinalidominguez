
from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
<<<<<<< HEAD
    subject = models.CharField(max_length=255)
    body = models.TextField()
    is_read = models.BooleanField(default=False)  # Asegúrate de que este campo tenga un valor por defecto

    def __str__(self):
        return f"Message from {self.sender} to {self.recipient}"
=======
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender} to {self.recipient} at {self.timestamp}"


class Page(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    code = models.CharField(max_length=255, default="")

    def save(self, *args, **kwargs):
        if not self.code:  
            self.code = f"PAGE-{self.id}"
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
>>>>>>> 534342b4ae5503d6dd2e2af41764a4d597df42f3
