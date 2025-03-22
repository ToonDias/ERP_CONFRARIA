from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/categoria', views.CadastrarCategoria, name='cadastrar_categoria'),
    path('cadastrar/fornecedor', views.CadastrarFornecedor, name='cadastrar_fornecedor'),
    path('cadastrar/unidade', views.CadastrarUnidade, name='cadastrar_unidade'),
    path('cadastrar/fabricante', views.CadastrarFabricante, name='cadastrar_fabricante'),
    path('cadastrar/produto', views.CadastrarProduto, name='cadastrar_produto'),
    path('cadastrar/lote', views.CadastrarLote, name='cadastrar_lote'),
    path('cadastrar/local-estoque', views.CadastrarLocalEstoque, name='cadastrar_local_estoque'),
]