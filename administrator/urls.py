from django.urls import path
from administrator import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('about_admin/',views.about_admin, name='about_admin'),
    path('products/',views.products, name='products')
]