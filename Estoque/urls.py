from django.urls import path
from . import views

urlpatterns = [
    #urls categoria
    path('categoria/', views.CategoriaListView.as_view(), name='listar_categorias'),
    path('categoria/adicionar/', views.CategoriaCreateView.as_view(), name='nova_categoria'),
    path('categoria/atualizar/<int:pk>', views.CategoriaUpdateView.as_view(), name='editar_categoria'),
    path('categoria/detalhes/<int:pk>', views.CategoriaDetailView.as_view(), name='detalhes_categoria'),
    path('categoria/deletar/<int:pk>', views.CategoriaDeleteView.as_view(), name='deletar_categoria'),
    # urls Fabricantes
    path('fabricantes/', views.FabricanteListView.as_view(), name='listar_fabricates'),
    path('fabricante/adicionar', views.FabricanteCreateView.as_view(), name='novo_fabricante'),
    path('fabricante/atualizar/<int:pk>', views.FabricanteUpdateView.as_view(), name='editar_fabricante'),
    path('fabricante/detalhes/<int:pk>', views.FabricanteDetailView.as_view(), name='detalhes_fabricante'),
    path('fabricante/deletar/<int:pk>', views.FabricanteDeleteView.as_view(), name='deletar_fabricante'),
    #urls outros
    path('cadastrar/fornecedor', views.CadastrarFornecedor, name='cadastrar_fornecedor'),
    path('cadastrar/unidade', views.CadastrarUnidade, name='cadastrar_unidade'),
    path('cadastrar/fabricante', views.CadastrarFabricante, name='cadastrar_fabricante'),
    path('cadastrar/produto', views.CadastrarProduto.as_view(), name='cadastrar_produto'),
    path('cadastrar/lote', views.CadastrarLote, name='cadastrar_lote'),
    path('cadastrar/local-estoque', views.CadastrarLocalEstoque, name='cadastrar_local_estoque'),
]