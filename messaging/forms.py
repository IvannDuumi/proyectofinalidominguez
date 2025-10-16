from django import forms
from .models import Message

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'birth_date', 'avatar']