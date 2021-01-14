from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
   path('submit/', views.consulta_bin, name='consulta_bin'),
   path('',views.index,name="index"),
]
