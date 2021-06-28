from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirm'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'password1', 'password2')
        
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email'}),
            'full_name': forms.TextInput(attrs={'placeholder':'Full Name'}),
        }
