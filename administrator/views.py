from django.shortcuts import render
from core.models import Product

# Create your views here.

def dashboard(request):
    return render(request,'admin/dashboard.html') 
def about_admin(request):
    return render(request,'admin/about_admin.html' )
def products(request):
    products = Product.objects.filter(status=1)
    context = {
         'products' : products,
    }
    return render(request,'admin/products.html',context)