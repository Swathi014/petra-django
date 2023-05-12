from django.urls import path
# f,rom core.views import index,about
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('marble/', views.marble, name='marble'),
    path('project/', views.marble, name='project'),
    path('contact/', views.marble, name='contact')
]