

from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('products/<str:pk>/', views.products, name="products"),
    path('product/<str:pk>/', views.product, name="product"),  
    path('cart/', views.cart, name="cart"),  
    path('order/', views.order, name="order"),  
    
    path('login/', views.loginPage, name="login"), 
    path('register/', views.registerPage, name="register"), 
    path('logout/', views.logoutUser, name="logout"), 
    
    path('profile/<str:pk>/', views.userProfile, name="profile"), 
    path('edit-profile/<str:pk>/', views.editProfile, name="edit-profile"), 
    path('addcart/<str:pk>/', views.addCart, name="addcart"),
    path('deleteitem/<str:pk>/', views.deleteItem, name="deleteitem"),
]
