from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.CharField(label='Nome de usuário', max_length=100)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
