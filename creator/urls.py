

from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('rigs/', views.creator, name="creator"),
    path('beads/', views.beads, name="beads"),
    path('decor/', views.decor, name="decor"),
]
