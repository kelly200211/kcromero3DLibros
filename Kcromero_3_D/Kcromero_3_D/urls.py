"""Kcromero_3_D URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('', views.login , name='login'),
    path('Home', views.Inicio , name='home'),
    path('crud', views.admin , name='crud'),
    path('Inicio_Sesion',views.Inicio_sesion, name='InicioLogin'),
    # crear
    path('LibroC',views.Crear_Libro, name='crearl'),
    path('LibroG',views.Crear_Genero, name='crearg'),
    path('LibroP',views.Crear_Prestamo, name='crearp'),

    # mostrar datos en el formulario actualizar
    path('ActualizarL/<int:id>',views.Actualizar_Libro_mostrar, name='Actualizarl'),
    path('ActualizarG/<int:id>',views.Actualizar_Genero_mostrar, name='Actualizarg'),
    path('ActualizarP/<int:id>',views.Actualizar_Prestamo_mostrar, name='Actualizarp'),

    # Actualizar 
    path('Actualizar_Libro/', views.Actualizar_Libro, name='ActualizarLi'),
    path('actualizar_genero/', views.Actualizar_Genero, name='Actualizarge'),
    path('Actualizar_prestamo/', views.Actualizar_Prestamo, name='ActualizarLi'),

    
    # eliminar
    path('EliminarL/<int:id>',views.Delete_Libro, name='eliminarl'),
    path('EliminarG/<int:id>',views.Delete_Genero, name='eliminarg'),
    path('EliminarP/<int:id>',views.Delete_Prestamo, name='eliminarp'),

    # ver Informacion usando mi modelo Detalle_libro
    path('Informacion/<int:id>', views.Informacion, name='Informacion'),



    path('admin/', admin.site.urls),
]
