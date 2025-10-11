
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'bio': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Contanos un poco sobre vos...'
            }),
        }
