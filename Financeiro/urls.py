from django.urls import path
from . import views

urlpatterns = [
    # PlanoContas urls
    path('planos-contas/', views.PlanoContasListView.as_views(), name='listar_planos'),
    path('planos-contas/adicionar/', views.PlanoContasCreateView.as_views(), name='novo_plano'),
    path('planos-contas/atualizar/<int:pk>', views.PlanoContasUpdateView.as_views(), name='editar_plano'),
    path('planos-contas/detalhes/<int:pk>', views.PlanoContasDetailView.as_views(), name='detalhes_plano'),
    path('planos-contas/detelar/<int:pk>', views.PlanoContasDeleteView.as_views(), name='deletar_plano'),
    # Outras URLs
    path('cadastrar/empresa', views.CadastrarEmpresa, name='cadastrar_empresa'),
    path('cadastrar/funcionario', views.CadastrarFuncionario, name='cadastrar_funcionario'),
    path('cadastrar/plano-contas', views.CadastrarPlanoContas, name='cadastrar_plano_contas'),path('planos/contas', views.PlanoContas.as_views(), name=''),
    path('cadastrar/ponto-recebimento', views.CadastrarPontoRecebimento, name='cadastrar_ponto_recebimento'),
    path('cadastrar/caixa-lancamento', views.CaixaLancamento, name='caixa_lancamento'),
    path('cadastrar/caixa-repasse', views.CaixaRepasse, name='caixa_repasse'),
]