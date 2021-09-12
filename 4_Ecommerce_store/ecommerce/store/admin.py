from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Customer)
class customerAdmin(admin.ModelAdmin):
    list_display=['id','user','name','email']

@admin.register(models.Product)
class productAdmin(admin.ModelAdmin):
    list_display=['id','name','price','digital']

@admin.register(models.Order)
class orderAdmin(admin.ModelAdmin):
    list_display=['id','customer','date_ordered','complete','transaction_id']

@admin.register(models.OrderItem)
class orderItemAdmin(admin.ModelAdmin):
    list_display = ['id','product','order','quantity','date_added']

@admin.register(models.ShippingAddress)
class shippingAddressAdmin(admin.ModelAdmin):
    list_display=['id','customer','order','address','city','state','zipcode','date_added']