from django.urls import path
from . import views

urlpatterns = [
    path('pedido/', views.PedidoListView.as_view(), name='listar_pedidos'),
    path('pedido/adicionar', views.PedidoCreateView.as_view(), name='novo_pedido'),
    path('pedido/atualizar/<int:pk>', views.PedidoUpdateView.as_view(), name='editar_pedido'),
    path('pedido/detalhes/<int:pk>', views.PedidoDetailView.as_view(), name='detalhes_pedido'),
    path('pedido/deletar/<int:pk>', views.PedidoDeleteView.as_view(), name='deletar_pedido'),
]