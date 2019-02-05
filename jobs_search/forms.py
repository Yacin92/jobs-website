from django.contrib.auth.models import User
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):

    username = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    status = forms.ChoiceField(widget=forms.RadioSelect(attrs={}), choices=Profile.STATUS)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'status']


class UserLoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
