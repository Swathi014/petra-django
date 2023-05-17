from django.shortcuts import render
from core.models import Carousal,Category,Product,Abouthome,Logo_slider,Project

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
    projects = Project.objects.all()

    # total_sections = projects.count() / 5

    # sections = []

    # for project in projects:
    #     i = 1
    #     project = {'project':project,'section':i}
    #     sections.append(project)

    section1 = Project.objects.all()[:5]
    section2 = Project.objects.all()[6:10]
    section3 = Project.objects.all()[11:15]

    context = {
        'projects' : projects,
        'section1' : section1,
        'section2' : section2,
        'section3' : section3,
    }
    return render(request,'projects.html',context)

def contact(request):
    return render(request,'contact.html')


    