from django.shortcuts import render
from .forms import imageForm

# Create your views here.
def index(request):
    if request.method=="POST":
        form=imageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = imageForm()
    return render(request,'main/index.html',{
        'form':form,
    })