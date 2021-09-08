from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class postModel(admin.ModelAdmin):
    list_display=['id','author','title','content','date','user_post']