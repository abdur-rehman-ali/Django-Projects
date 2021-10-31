from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _

class registrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }),
    label='Password',
    label_suffix='')
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control '
    }),
    label='Confirm Password',
    label_suffix='')
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {
            'username':'Username',
            'email':'Email'
        }
        labels_suffix = {
            'username':'',
            'email':''
        }
        widgets={
            'username':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control'
            }),
        }
        