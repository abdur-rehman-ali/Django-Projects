from django.forms import ModelForm
from main.models import posts

class postForm(ModelForm):
    class Meta:
        model = posts
        fields = '__all__'