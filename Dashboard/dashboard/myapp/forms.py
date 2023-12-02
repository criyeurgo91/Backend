from django import forms
from .models import *

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name_userProfile', 'lastname_userProfile', 'phone_userProfile', 'ismander_userProfile']









