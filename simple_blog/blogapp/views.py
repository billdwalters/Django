import user

from django.shortcuts import render
from django.http import HttpResponse
from models import BlogArticle
from django.contrib.auth import authenticate, login




# Create your views here.

def index(request):
    blogs = BlogArticle.objects.all()
    if request.method == 'POST':
        usname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=usname, password=pwd)
        if user is not None:
            login(request,user)
            return render(request, "main.html", {'testvar':"Test String 3!",'blogs':blogs, 'user':user})
    return render(request, "main.html", {'testvar':"Test String 222 !!!",'blogs' :blogs, 'user':None})

def createblog(request):
    readblog = BlogArticle()
    readblog.title = request.POST["title"]
    readblog.author = request.user
    readblog.blog_content = request.POST['blog_content']
    readblog.save()
    return render(request, "Main.html", {'testvar':"My new view !!!",'blogs':blogs, 'user':user})
