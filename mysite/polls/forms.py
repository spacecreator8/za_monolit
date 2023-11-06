from django import forms
from .models import *


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'username', 'mail', 'password', 'password2', 'avatar']
        widgets = {
            'password': forms.PasswordInput(attrs={'name': 'password', 'type': 'password', 'autocomplete': 'off'}),
            'password2': forms.PasswordInput(attrs={'name': 'password2', 'type': 'password', 'autocomplete': 'off'}),
        }
