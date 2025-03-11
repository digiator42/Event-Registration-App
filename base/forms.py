from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from .models import Submission


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'password1']
           
class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['details']