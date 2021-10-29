from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class posts(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField(blank=True)
