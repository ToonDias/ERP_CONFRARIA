from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/pedido', views.CadastrarPedido, name='cadastrar_pedido'),
    path('consultar/pedido', views.ConsultarPedido, name='consultar_pedido'),
]