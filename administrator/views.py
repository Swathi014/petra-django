from django.shortcuts import render,redirect
from core.models import Product,Category
from django.contrib import messages

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
    if request.method == 'POST':
        title = request.POST.get('category_name')
        image = request.FILES.get('category_image')
        inner_title = request.POST.get('category_innertitle')
        inner_subtitle = request.POST.get('category_innersubtitle')
        subtitle = request.POST.get('category_subtitle')
        description = request.POST.get('category_description')
        
        Category.objects.create(image=image,title=title,inner_title=inner_title,inner_subtitle=inner_subtitle,sub_title=subtitle,description=description)
        messages.success(request,'New category created')
        return redirect('categories')

    return render(request,'admin/add-category.html')


def edit_category(request,category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            category.image = request.FILES.get('category_image')
        category.title = request.POST.get('category_name')
        category.inner_title = request.POST.get('category_innertitle')
        category.inner_subtitle = request.POST.get('category_innersubtitle')
        category.subtitle = request.POST.get('category_subtitle')
        category.description = request.POST.get('category_description')
        category.save()
        return redirect('categories')
    context = {
        'category' : category,
    }
    return render(request,'admin/edit-category.html',context)