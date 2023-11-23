from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.IntegerField(label='username', required=True)
    password = forms.CharField(label='password', required=True)
    class Meta:
        fields = ['username', 'password']