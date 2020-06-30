from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.weatherview),
    path('delete/<name>/',views.deleteview,name='delete'),
]
