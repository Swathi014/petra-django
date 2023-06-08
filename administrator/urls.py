from django.urls import path
from administrator import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('about_admin/',views.about_admin, name='about_admin'),
    path('products/',views.products, name='products'),
    path('add-product/',views.add_products, name='add_products'),
    path('categories/',views.category, name='categories'),
    path('add-category/',views.add_categories, name='add_categories')
]