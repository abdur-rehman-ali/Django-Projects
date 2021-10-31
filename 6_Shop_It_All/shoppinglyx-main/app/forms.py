from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
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
        

class logInForm(AuthenticationForm):
    username = forms.CharField(max_length=254,widget=forms.TextInput(attrs={
        'class':'form-control'
    }),
    label_suffix='')
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }),
    label_suffix='')

class changePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old password"),
                                   widget=forms.PasswordInput(attrs={
                                       'class':'form-control'
                                   }))
    new_password1 = forms.CharField(label=_("New password"),
                                    widget=forms.PasswordInput(attrs={
                                       'class':'form-control'
                                   }))
    new_password2 = forms.CharField(label=_("Confirm new password ? "),
                                    widget=forms.PasswordInput(attrs={
                                        'class':'form-control'
                                    }))
