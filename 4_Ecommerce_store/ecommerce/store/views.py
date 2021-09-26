from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Product,Order,OrderItem
import json
# Create your views here.

def store(request):
	all_products = Product.objects.all()
	if request.user.is_authenticated:
		customer=request.user.customer
		order,created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()

	else:
		items=[]
		order={
			'get_total_cart_items':0,
			'get_cart_total':0
			}
	
	context = {'all_products':all_products,'order':order}
	return render(request, 'store/store.html', context)

def cart(request):
	if request.user.is_authenticated:
		customer=request.user.customer
		order,created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()

	else:
		items=[]
		order={
			'get_total_cart_items':0,
			'get_cart_total':0
			}
	context = {'items':items,'order':order}
	return render(request, 'store/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer=request.user.customer
		order,created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()

	else:
		items=[]
		order={
			'get_total_cart_items':0,
			'get_cart_total':0
			}
	context = {'items':items,'order':order}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	product_id = data['product_id']
	action = data['action']
	
	customer = request.user.customer
	product = Product.objects.get(id=product_id)

	order,created = Order.objects.get_or_create(customer=customer,complete=False)

	orderitem,created = OrderItem.objects.get_or_create(order=order,product=product)

	#This will increment the cart value with up arrow is pressed
	if action == 'add':
		orderitem.quantity = orderitem.quantity+1
	#This will decrement the cart value with down arrow is pressed
	elif action == 'remove':
		orderitem.quantity = orderitem.quantity -1
	orderitem.save()

	if orderitem.quantity<=0:
		orderitem.delete()


	return JsonResponse('item added to cart successfully',safe=False)