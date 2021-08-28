from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.ToDoListData)
class ToDoListDataDisplay(admin.ModelAdmin):
    list_display=['id','task']