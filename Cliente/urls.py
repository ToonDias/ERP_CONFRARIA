from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.ListarClientes, name='ListarClientes'),
    path('consultar', views.ConsultarCliente, name='ConsultarCliente')
]