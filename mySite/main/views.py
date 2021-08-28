from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoListData
from .forms import ToDoListForm

# Create your views here.
def index(request):
    form=ToDoListForm(auto_id=True)
    return render(request,'main/index.html',{
        'form':form
    })

def showItems(request):
    data=ToDoListData.objects.all()
    return render(request,'main/showItem.html',{
        'data':data
    })