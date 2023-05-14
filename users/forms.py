from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required.Add a valid email address")

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use")
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        try:
            user = User.objects.get(username =username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"Email {username} is already in use")