from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from postdisplay.models import postview

def login(request):
    return render(request,"index.html")

def homepage(request):
    postData = postview.objects.all()
    if request.method =="GET":
        st = request.GET.get('postname')
        if st != None:
            postData = postview.objects.filter(post_title__icontains=st)
    
    data = {
        'postData': postData
    }
    return render(request,"home.html",data)

def postDetails(request,slug):
    postdetails = postview.objects.get(slug=slug)
    data={
        'postdetails': postdetails
    }
    return render(request,"postdetails.html",data)

def createPost(request):
    return render(request,"createpost.html")

def savePost(request):
    if request.method=="POST":
        pt = request.POST.get('postTitle')
        pd = request.POST.get('postDetails')
        post = postview(post_title=pt,post_details=pd)
        post.save()
    return render(request,"createpost.html")