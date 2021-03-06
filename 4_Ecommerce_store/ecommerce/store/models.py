from django.db import models
from django.contrib.auth.models import User
from django.db.models import  AutoField

# Create your models here.

# 1-1 Relationship with user 
class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete =models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True, blank=True)
    image = models.ImageField(blank=True) 


    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

    def __str__(self):
	    return self.name

# 1-M relationship with customer
class Order(models.Model):
    id=models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    @property
    def get_cart_total(self):
        items_ordered=self.orderitem_set.all()
        total_cart_price = sum([item.get_total for item in items_ordered])
        return total_cart_price

    @property
    def get_total_cart_items(self):
        items_ordered=self.orderitem_set.all()
        total_cart_price = sum([item.quantity for item in items_ordered])
        return total_cart_price

    def __str__(self):
	    return str(self.id)

#1-M relationship with product
#1-M relationship with order
class OrderItem(models.Model):
    id=models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.product.price * self.quantity

#1-M relationship with customer
#1-M relationship with order
class ShippingAddress(models.Model):
    id=models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
	    return self.address
