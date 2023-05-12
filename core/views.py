from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def marble(request):
    return render(request,'marble.html')

def project(request):
    return render(request,'project.html')

def project(request):
    return render(request,'contact.html')