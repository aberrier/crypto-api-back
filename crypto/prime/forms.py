from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    """
    Custom form to allow email input
    """
    class Meta:
        model = User
        fields = ("username", "email")
        field_classes = {'username': UsernameField}


class CustomUserChangeForm(UserChangeForm):
    """
    Custom form to allow email input
    """
    class Meta:
        model = User
        fields = ("username", "email")
        field_classes = {'username': UsernameField}
