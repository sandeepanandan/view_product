from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': "text",'placeholder': 'Your Name'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'type': "email",'placeholder': 'Your Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': "password", 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': "password",
               'placeholder': 'Reapet Your Password'}))

    class meta:
        model = User
        fields = [
            'first_name',
            'email',
            'password1',
            'password2',
        ]


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': "text", 'placeholder': 'UserName'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': "password", 'placeholder': 'Password'}))



