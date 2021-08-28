from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoListData


# Create your views here.
def index(request):
    return render(request,'main/index.html')

def showItems(request):
    data=ToDoListData.objects.all()
    return render(request,'main/showItem.html',{
        'data':data
    })