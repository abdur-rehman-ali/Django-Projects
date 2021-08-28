from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
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
            form=ToDoListForm(auto_id=True)
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


#This function will delete data
def deleteItems(request,id):
    if request.method=="POST":
        data = ToDoListData.objects.get(pk=id)
        data.delete()
    return HttpResponseRedirect("/show/")

def updateItems(request,id):
    if request.method=="POST":
        form=ToDoListForm(request.POST)
        if form.is_valid():
            task=form.cleaned_data['task']
            data = ToDoListData(id=id,task=task)
            data.save()

    else:
        data =ToDoListData.objects.get(pk=id)
        form = ToDoListForm(initial={
        'task':data.task
    })
    return render(request,"main/update.html",{
        'form':form,
        'id':id,
    })