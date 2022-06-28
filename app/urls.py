from operator import index
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name = ''),
    path("base/", base, name='base'),
    path("index/", index, name='index'),
    path("login/",login, name='login'),
    path("registro/",registro, name='registro'),
    path("index_login/", index_login, name='index_login'),
    path("historial/",historial, name='historial'),
    path("productos/",productos, name='productos'),
    path("seguimiento/", seguimiento, name='seguimiento'),

    path("agregarProductos/", agregarProductos, name='agregarProductos'),
    path("listarProductos/",listarProductos, name='listarProductos'),
    path("modificarProductos/<codigo>/",modificarProductos, name='modificarProductos'),
    path("eliminarProductos/<codigo>/",eliminarProductos, name='eliminarProductos'),
    path("apiex/", apiex, name = 'apiex'),

    path("agregarClientes/",agregarClientes, name='agregarClientes'),
    path("listarClientes/",listarClientes, name='listarClientes'),
    path("eliminarClientes/<codigo>/",eliminarClientes, name='eliminarClientes'),
    path("modificarClientes/<codigo>/",modificarClientes, name='modificarClientes'),

    path("carritoCompras/",carritoCompras, name='carritoCompras'),
    path("compraExitosa/",compraExitosa, name='compraExitosa'),
]