from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'email', 'password1', 'password2')
