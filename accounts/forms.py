<<<<<<< HEAD
# accounts/forms.py
=======
>>>>>>> a59227e5c5c30dd1ae5685e3d4ce921d8ce9bf8d
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta:
<<<<<<< HEAD
        model = Profile
        fields = ['avatar', 'bio', 'birth_date', 'first_name', 'last_name']  # Se agregan los campos de nombre y apellido
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Contanos un poco sobre vos...'}),
        }
=======
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
>>>>>>> a59227e5c5c30dd1ae5685e3d4ce921d8ce9bf8d
