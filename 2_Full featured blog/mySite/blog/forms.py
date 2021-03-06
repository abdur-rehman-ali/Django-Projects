from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import User
from django import forms
from .models import Post

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

class logInForm(AuthenticationForm):
    username = forms.CharField(max_length=254,widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))
        
class userDataUpdateForm(UserChangeForm):
    password = None
    class Meta:
        model=User
        fields=('username','first_name','last_name','email')
        widgets={
            'username':forms.TextInput(attrs={
            'class':'form-control'}),
            'first_name':forms.TextInput(attrs={
            'class':'form-control'}),
            'last_name':forms.TextInput(attrs={
            'class':'form-control'}),
            'email':forms.TextInput(attrs={
            'class':'form-control'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ('title','content')
        widgets={
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Title',
            }),
            'content':forms.Textarea(attrs={
                'rows':20,
                 'placeholder':'Content',
            }),
        }
        labels={
            'title':'',
            'content':''
        }