from django.shortcuts import render
from core.models import Carousal

# Create your views here.
def index(request):
    carousals = Carousal.objects.first()
    context = {
        'carousals' : carousals
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def marble(request):
    return render(request,'marble.html')

def project(request):
    return render(request,'project.html')

def project(request):
    return render(request,'contact.html')