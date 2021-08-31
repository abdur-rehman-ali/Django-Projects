from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class signInForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control '
    }))
    class Meta:
        model=User
        fields=('username','email')
        labels={
            'username':'Username',
            'email':'Email'
        }
        widgets={
            'username':forms.TextInput(attrs={
                'class':'form-control '
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control '
            })
        }
