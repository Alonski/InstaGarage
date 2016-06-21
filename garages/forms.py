from django import forms
from mptt.forms import TreeNodeChoiceField
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length=300)
    password = forms.CharField(max_length=300, widget=forms.PasswordInput())


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=300)
    last_name = forms.CharField(max_length=300)
    username = forms.CharField(max_length=300)
    password = forms.CharField(max_length=300, widget=forms.PasswordInput())
    password_recheck = forms.CharField(max_length=300, widget=forms.PasswordInput())
    email = forms.EmailField(max_length=300)
    manufacturer = forms.CharField(max_length=30, widget=forms.HiddenInput)
    make = forms.CharField(max_length=30, widget=forms.HiddenInput)
    year = forms.DateField(widget=forms.HiddenInput)
    # worker_id = forms.IntegerField()
