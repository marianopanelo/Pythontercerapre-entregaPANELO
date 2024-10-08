"""
URL configuration for tercera_pre_entrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tercera_pre_entrega import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.index,name = 'inicio'),
    path('loguin/', views.loguin,name = 'loguin'),
    path('cabañas/', views.cabanas,name = 'cabañas'),
    path('reservar/', views.reservar,name = 'reservar'),
    path('miReserva/', views.mis_reservas,name = 'miReserva'),
    path('comentanos/', views.comentanos,name = 'comentanos'),
    path('codigo/', views.resultado_busqueda_reserva,name = 'resultado_busqueda_reserva'),
]
