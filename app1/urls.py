from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fecha-actual/', views.fecha_actual, name='fecha_actual'),
]