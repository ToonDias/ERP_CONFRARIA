from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.ListarClientes, name='listar_clientes'),
    #path('consultar/', views.ConsultarCliente, name='consultar_clientes'),
    path('cadastrar/pessoa-fisica', views.CadastrarPessoaFisica, name='cadastrar_pessoa_fisica'),
    path('cadastrar/pessoa-juridica', views.CadastrarPessoaJuridica, name='cadastrar_pessoa_juridica'),
    path('cadastrar/pessoa-fisica-estrangerida', views.CadastrarPessoaFisicaEstrangeira, name='cadastrar_pessoa_fisica_estrangeira'),
    path('cadastrar/pessoa-juridica-estrangeira', views.CadastrarPessoaJuridicaEstrangeira, name='cadastrar_pessoa_juridica_estrangeira'),

    # Search views
     path('consultar/', views.cliente_search_view, name='consultar_clientes'),
]