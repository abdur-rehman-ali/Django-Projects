from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render,HttpResponseRedirect
from .forms import registrationForm ,logInForm,changePasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import product


def home(request):
    trousers = product.objects.filter(category='TROUSER')
    suits = product.objects.filter(category='SUIT')
    shorts = product.objects.filter(category='SHORT')
    shirts = product.objects.filter(category='SHIRT')

    context = {
        'trousers':trousers,
        'suits':suits,
        'shorts':shorts,
        'shirts':shirts,
    }
    template_name = 'app/home.html'
    return render(request,template_name,context)

def product_detail(request,id):
    products = product.objects.get(id=id)
    context = {
        'product':products
    }
    template_name = 'app/productdetail.html'
    return render(request, template_name,context)

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = changePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return HttpResponseRedirect('/')
    else:
        form =changePasswordForm(user=request.user)
    context = {
            'form':form
        }
    template_name = 'app/changepassword.html'
    return render(request, template_name,context)


def mobile(request):
 return render(request, 'app/mobile.html')

def customerlogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            form = logInForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upassword = form.cleaned_data['password']
                user = authenticate(username=uname,password=upassword)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/')
        else:
            form = logInForm()
        context = {
            'form':form
        }
        template_name = 'app/login.html'
        return render(request, template_name,context)

def customerregistration(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method=='POST':
            form = registrationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('login/')

        else:
            form = registrationForm()
        context = {
            'form':form
        }
        template_name = 'app/customerregistration.html'
        return render(request, template_name,context)

@login_required(login_url='/login/')
def customerlogout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/')

def checkout(request):
 return render(request, 'app/checkout.html')
