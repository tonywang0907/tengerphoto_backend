from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('images/<str:category>/', views.getImages, name='images')
]