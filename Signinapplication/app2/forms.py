from django import forms
from django.contrib.auth.models import User
from app2.models import UserProfileInfo


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput, max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')



class UserProfileForm(forms.ModelForm):
    portfolio_site = forms.URLField(widget=forms.URLInput())
    profile_pic = forms.ImageField(widget=forms.FileInput(), required=False)
    
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')