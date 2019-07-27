from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

def welcome(request):
    return render(request, 'funccrud/index.html')

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'funccrud/funccrud.html', {'blogs':blogs})

def create(request):
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = NewBlog()
        return render(request, 'funccrud/new.html', {'form':form})
def update(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    form = NewBlog(request.POST,instance=blog)

    if form.is_valid():
       form.save()
       return redirect('home')

    return render(request, 'funccrud/new.html',{'form':form})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')

def signup(request):
    if request.method == 'POST':
       if request.POST['password1'] == request.POST['password2']:
          user = User.objects.create_user(request.POST['username'])
          password = request.POST['password1']
          auth.login(request,user)
       return redirect('home')
    return render(request, 'funccrud/signup.html')

def login(request):
    if request.method =='POST':
       username = request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(request, username=username, password=password)
       if user is not None:
          auth.login(request, user)
          return redirect('home')
       else:
          return render(request, 'funccrud/login.html', {'error': 'username or password is incorrect.'})
    else:
       return render(request, 'funccrud/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def add_comment(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
           comment = form.save(commit=False)
           comment.post = blog
           comment.save()
           return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'funccrud/add_comment.html', {'form':form})

# Create your views here.
