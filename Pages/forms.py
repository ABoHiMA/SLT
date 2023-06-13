from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
      username = forms.CharField(label='Username')
      first_name = forms.CharField(label='First Name')
      last_name = forms.CharField(label='Last Name')
      email = forms.EmailField(label='Email')
      password1 = forms.CharField(label='Password', widget=forms.PasswordInput(), min_length=8)
      password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(), min_length=8)
      class Meta:
            model = User
            fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class FeedbackForm(forms.Form):
    username = forms.CharField(label='Username')
    text = forms.CharField()

        