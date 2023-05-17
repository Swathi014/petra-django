from django.shortcuts import render
from core.models import Carousal,Category,Product,Abouthome,Logo_slider

# Create your views here.
def index(request):
    carousals = Carousal.objects.all() 
    categories = Category.objects.all()
    abouthome = Abouthome.objects.last()
    products = Product.objects.filter(status=1)
    logo_slider = Logo_slider.objects.all()
    context = {
        'carousals' : carousals,
        'categories' : categories,
        'abouthome' : abouthome,
        'products' : products,
        'logo_sliders' : logo_slider
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def category(request,category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    context = {
        'category' : category,
        'products' : products
    }
    return render(request,'marble.html',context)

def project(request):
    return render(request,'project.html')

def contact(request):
    return render(request,'contact.html')


    