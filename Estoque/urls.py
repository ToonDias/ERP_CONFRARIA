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
    path('fabricantes/', views.FabricanteListView.as_view(), name='listar_fabricantes'),
    path('fabricante/adicionar', views.FabricanteCreateView.as_view(), name='novo_fabricante'),
    path('fabricante/atualizar/<int:pk>', views.FabricanteUpdateView.as_view(), name='editar_fabricante'),
    path('fabricante/detalhes/<int:pk>', views.FabricanteDetailView.as_view(), name='detalhes_fabricante'),
    path('fabricante/deletar/<int:pk>', views.FabricanteDeleteView.as_view(), name='deletar_fabricante'),
    # urls Unidade
    path('unidades/', views.UnidadeListView.as_view(), name='listar_unidades'),
    path('unidade/adicionar', views.UnidadeCreateView.as_view(), name='nova_unidade'),
    path('unidade/atualizar/<int:pk>', views.UnidadeUpdateView.as_view(), name='editar_unidade'),
    path('unidade/detalhes/<int:pk>', views.UnidadeDetailView.as_view(), name='detalhes_unidade'),
    path('unidade/delete/<int:pk>', views.UnidadeDeleteView.as_view(), name='deletar_unidade'),
    # urls Local de estoque
    path('local-estoque/', views.LocalEstoqueListView.as_view(), name='listar_locais'),
    path('local-estoque/adicionar', views.LocalEstoqueCreateView.as_view(), name='novo_local'),
    path('local-estoque/atualizar/<int:pk>', views.LocalEstoqueUpdateView.as_view(), name='editar_local'),
    path('local-estoque/detalhes/<int:pk>', views.LocalEstoqueDetailView.as_view(), name='detalhes_local'),
    path('local-estoque/deletar/<int:pk>', views.LocalEstoqueDeleteView.as_view(), name='deletar_local'),
    # urls Produto
    path('produto/', views.ProdutoListView.as_view(), name='listar_produtos'),
    path('produto/adicionar', views.ProdutoCreateViews.as_view(), name='novo_produto'),
    path('produto/atualizar/<int:pk>', views.ProdutoUpdateViews.as_view(), name='editar_produto'),
    path('produto/detalhes/<int:pk>', views.ProdutoDetailView.as_view(), name='detalhes_produto'),
    path('produto/detelar/<int:pk>', views.ProdutoDeleteView.as_view(), name='deletar_produto'),
    #urls Lotes
    path('lote/', views.LoteListView.as_view(), name='listar_lotes'),
    path('lote/adicionar', views.LoteCreateView.as_view(), name='novo_lote'),
    path('lote/atualizar/<int:pk>', views.LoteUpdateView.as_view(), name='editar_lote'),
    path('lote/detalhes/<int:pk>', views.LoteDetailView.as_view(), name='detalhes_lote'),
    path('lote/deletar/<int:pk>', views.LoteDeleteView.as_view(), name='deletar_lote'),
    #urls Fornecedor
    path('fornecedor/', views.FornecedorListView.as_view(), name='listar_fornecedores'),
    path('fornecedor/adicionar', views.FornecedorCreateView.as_view(), name='novo_fornecedor'),
    path('fornecedor/editar/<int:pk>', views.FornecedorUpdateView.as_view(), name='editar_fornecedor'),
    path('fornecedor/detalhes/<int:pk>', views.FornecedorDetailView.as_view(), name='detalhes_fornecedor'),
    path('fornecedor/deletar/<int:pk>', views.FornecedorDeleteView.as_view(), name='deletar_fornecedor'),   
]