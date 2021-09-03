from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
from .forms import signInForm,logInForm,userDataUpdateForm,PostForm
from .models import Post
import datetime

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html',{
        'posts':posts
    })


def about(request):
    return render(request,'blog/about.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user.username)
        return render(request,'blog/dashboard.html',{
            'posts':posts
        })
    else:
        return HttpResponseRedirect('/logIn/')

def addPost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PostForm(request.POST)
            if fm.is_valid():
                postTitle = fm.cleaned_data['title']
                postContent = fm.cleaned_data['content']
                postAuthor = request.user.username
                postDate = datetime.datetime.now()
                post = Post(title=postTitle,content=postContent,author=postAuthor,date=postDate)
                post.save()
                fm=PostForm()
        else:       
            fm=PostForm()
        return render(request,'blog/addPost.html',{
            'form':fm,
        })
    else:
        return HttpResponseRedirect('/logIn/')


def updatePost(request,id):
    if request.user.is_authenticated:
        post=Post.objects.get(pk=id)
        if request.method=="POST":
            fm=PostForm(request.POST,instance=post)
            if fm.is_valid():
                fm.save()
        else:
            fm = PostForm(instance=post)
        return render(request,'blog/updatePost.html',{
            'id':id,
            'form':fm
        })
    else:
        return HttpResponseRedirect('/logIn/')

def deletePost(request,id):
    if request.user.is_authenticated:
        post=Post.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/logIn/')


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm=userDataUpdateForm(data=request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
        else:
            fm=userDataUpdateForm(instance=request.user)
        return render(request,'blog/profile.html',{
            'form':fm
        })
    else:
        return HttpResponseRedirect('/logIn/')

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
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/')
        else:        
            fm=logInForm()
        return render(request,'blog/logIn.html',{
            'form':fm
        })

def logOut_view(request):
    logout(request)
    return HttpResponseRedirect('/logIn/')


