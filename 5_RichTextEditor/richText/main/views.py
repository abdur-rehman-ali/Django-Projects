from django.shortcuts import render
from .models import posts
from .forms import postForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            form.save()
            form = postForm()
    else:
        form = postForm()
    template_name = 'main/index.html'
    context={
        'form':form
    }
    return render(request, template_name, context)

def allPosts(request):
    template_name = 'main/data.html'
    data = posts.objects.all()
    context={
        'data':data
    }
    return render(request,template_name, context)