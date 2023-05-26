from django.urls import path
# f,rom core.views import index,about
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('project/', views.project, name='project'),
    path('contact/', views.contactview, name='contact'),
]