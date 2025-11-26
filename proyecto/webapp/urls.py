# webapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Esta es la URL vacía dentro de la aplicación
    path('', views.inicio, name='inicio'), 
]   