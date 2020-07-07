from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import Category, Post, Comment, Signup
from .forms import commentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def index(request):
    post = Post.objects.order_by('-timestamp')[:3]
    print(post)
    context = {'post': post}
    return render(request, 'blog/index.html', context)


def blog(request):
    post = Post.objects.all()
    context = {'post': post}
    return render(request, 'blog/blog.html', context)


def postPage(request, id):
    post = Post.objects.get(sno=id)
    showcomment = Comment.objects.filter(postby=id).filter(parent=None)
    form = commentForm()
    if request.method == "POST":
        form = commentForm(request.POST)
        form.instance.postby = post
        form.instance.commentBy = request.user
        parent = request.POST.get('parent')
        
        if parent:
            parentpost = Comment.objects.get(id= parent)
            form.instance.parent = parentpost

        if form.is_valid():
            form.save()
            return redirect('postpage', id=post.sno)
    
    context={'post':post, 'com':form, 'comment':showcomment}
    return render(request, 'blog/postpage.html', context)

def search(request):
    val = request.GET['search']

    byTitle = Post.objects.filter(title__icontains=val)
    byOverview = Post.objects.filter(overview__icontains=val)
    searchPost = byTitle.union(byOverview)
    context={'searchPost':searchPost}
    return render(request, 'blog/search.html', context)
    
def handleLogin(request):
    
    if request.method == "POST":
        loginusername = request.POST['loginusername']  
        loginpassword = request.POST['loginpassword']  

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request,'User Login')
            return redirect('index')
        else:
            messages.error(request,'Some Error Occure')
            print('not login')
            return redirect('index')
    else:
        return HttpResponse('404 -page Not Found')

def handleSignup(request):
    username = request.POST['username']
    email = request.POST['email']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']


    if request.method == "POST":
        if pass1 == pass2:
            try:
                user= User.objects.get(username=username)
                messages.error(request,'User Is Already Exist')
                return redirect('index')
            except User.DoesNotExist:
                signup = Signup(username=username, email=email, firstname=firstname, lastname=lastname, pass1=pass1, pass2=pass2)
                signup.save()
                myUser = User.objects.create_user(username, email, pass1, is_staff=True)
                myUser.first_name = firstname
                myUser.last_name = lastname
                myUser.save()
                messages.success(request,'User Successfully Register')
                return redirect('index')
        else:
            messages.error(request,'Password Not Match')
            return redirect('index')
    else:
        return HttpResponse(404)


def handleLogout(request):
    logout(request)
    return redirect('index')