from django.shortcuts import render
from .forms import imageForm
from .models import Image

# Create your views here.
def index(request):
    if request.method=="POST":
        form=imageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = imageForm()
    else:
        form = imageForm()
    images = Image.objects.all()
    return render(request,'main/index.html',{
        'form':form,
        'images':images,
    })