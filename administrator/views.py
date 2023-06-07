from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request,'admin/dashboard.html') 
def about_admin(request):
    return render(request,'admin/about_admin.html' )
def products(request):
    return render(request,'admin/products.html')