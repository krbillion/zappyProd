from django import forms
from .models import Profile,User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('location',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
