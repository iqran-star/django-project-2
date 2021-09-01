from django.shortcuts import render,redirect
from .models import Blog
from .forms import BlogForm
# Create your views here.
def index(request):
    blog=Blog.objects.all()
    return render(request,'blog/index.html',{'blogs':blog})

def create(request):
    if request.method=='POST':
        form=BlogForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
        
    form=BlogForm()
    return render(request,'blog/create.html',{'forms':form})

def detail(request,id):
    blog=Blog.objects.get(pk=id)
    return render(request,'blog/detail.html',{'blog':blog})    
def delete(request,id):
    blog=Blog.objects.get(pk=id)
    blog.delete()
    return redirect('/')