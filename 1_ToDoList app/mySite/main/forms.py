from django import forms

class ToDoListForm(forms.Form):
    task = forms.CharField(label='Task to do',label_suffix=" ",widget=forms.TextInput(attrs={
        'class':'form-control'
    }))