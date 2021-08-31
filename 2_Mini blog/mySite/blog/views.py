from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
from .forms import signInForm,logInForm
# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def about(request):
    return render(request,'blog/about.html')

def dashboard(request):
    return render(request,'blog/dashboard.html')

#Sign in page
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
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method=="POST":
            fm=logInForm(request=request,data=request.POST)
            print("POST REQUEST")
            print(fm.is_valid())
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                print("Inside valid")
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    print("Executed")
                    return HttpResponseRedirect('/')
        else:        
            fm=logInForm()
        return render(request,'blog/logIn.html',{
            'form':fm
        })

def logOut_view(request):
    logout(request)
    return HttpResponseRedirect('/logIn/')


