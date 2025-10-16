<<<<<<< HEAD
# messaging/forms.py
from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body']
=======
from django import forms
from .models import Message

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'birth_date', 'avatar']
>>>>>>> 534342b4ae5503d6dd2e2af41764a4d597df42f3
