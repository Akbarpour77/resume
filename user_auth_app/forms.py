from django import forms
from django.contrib.auth.models import User
from user_auth_app.models import UserProfile


class UserInfo(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User

        fields = ('username', 'email', 'password')


class UserProfileInfo(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('picture', 'url')
