from django.shortcuts import render,HttpResponseRedirect
from .forms import signInForm
# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def about(request):
    return render(request,'blog/about.html')

def dashboard(request):
    return render(request,'blog/dashboard.html')

def signIn_view(request):
    if request.method=="POST":
        fm=signInForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/logIn/')
    else:
        fm=signInForm()
    return render(request,'blog/signIn.html',{
        'form':fm
    })

def logIn_view(request):
    return render(request,'blog/logIn.html')

def logOut_view(request):
    pass


