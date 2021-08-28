from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoListData
from .forms import ToDoListForm

# Create your views here.
def index(request):
    if request.method=="POST":
        form = ToDoListForm(request.POST)
        if form.is_valid():
            task=form.cleaned_data['task']
            data=ToDoListData(task=task)
            data.save()
    else:
        form=ToDoListForm(auto_id=True)
    return render(request,'main/index.html',{
        'form':form
    })

def showItems(request):
    data=ToDoListData.objects.all()
    return render(request,'main/showItem.html',{
        'data':data
    })