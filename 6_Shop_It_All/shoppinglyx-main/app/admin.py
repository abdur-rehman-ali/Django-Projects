from django.contrib import admin
from .models import product

# Register your models here.
@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','brand','category','image']