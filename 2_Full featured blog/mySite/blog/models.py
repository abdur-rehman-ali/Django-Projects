from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content = RichTextField(blank=True)
    author=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)
    user_post=models.ForeignKey(User,on_delete=models.CASCADE)
