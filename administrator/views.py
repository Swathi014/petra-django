from django.shortcuts import render
from core.models import Product,Category

# Create your views here.

def dashboard(request):
    return render(request,'admin/dashboard.html') 
def about_admin(request):
    return render(request,'admin/about_admin.html' )
def products(request):
    products = Product.objects.all()
    context = {
         'products' : products,
    }
    return render(request,'admin/products.html',context)
def add_products(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories,
    }
    return render(request,'admin/add-product.html',context)
def category(request):
    categories = Category.objects.all()
    context = {
         'categories' : categories,
    }
    return render(request,'admin/categories.html',context)
def add_categories(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories,
    }
    return render(request,'admin/add-category.html',context)