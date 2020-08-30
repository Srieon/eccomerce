from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name= "Mall Home"),
    path('about/', views.about,name= "about"),
    path('contact/', views.contact,name= "contact"),
    path('product/<int:id>', views.prodview,name= "product"),
    path('cart/', views.cart,name= "cart"),
]
