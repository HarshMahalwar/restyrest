from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/create/', views.create, name='create'),
    path('/read/', views.read, name='read'),
    path('/update/<str:pk>/', views.update, name='update'),
    path('/delete/<str:pk>/', views.delete, name='delete'),
]
