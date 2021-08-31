from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def about(request):
    return render(request,'blog/about.html')

def dashboard(request):
    return render(request,'blog/dashboard.html')

def signIn_view(request):
    return render(request,'blog/signIn.html')

def logIn_view(request):
    return render(request,'blog/logIn.html')

def logOut_view(request):
    pass


