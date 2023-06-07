from django.urls import path
from administrator import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('blank/',views.blank, name='blank'),
]