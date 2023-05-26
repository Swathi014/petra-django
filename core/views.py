from django.shortcuts import render,redirect
from core.models import Carousal,Category,Product,Abouthome,Logo_slider,Project,enquiry,contact

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
    categories = Category.objects.all()
    context = {
        'category' : category,
        'products' : products,
        'categories' : categories
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

def contactview(request):
    cont = contact.objects.last()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')
        print('name : ',name,' email : ',email,' description : ', description)
        enquiry.objects.create(name=name,email=email,description=description)
        return redirect('.')
    
    context = {
        'contact': cont
    }
    return render(request,'contact.html',context)


    