from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render,HttpResponseRedirect
from .forms import registrationForm ,logInForm

def home(request):
 return render(request, 'app/home.html')

def product_detail(request):
 return render(request, 'app/productdetail.html')

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

def change_password(request):
 return render(request, 'app/changepassword.html')

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

def customerlogout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/')

def checkout(request):
 return render(request, 'app/checkout.html')
