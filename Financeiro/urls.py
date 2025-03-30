from django.urls import path
from . import views

urlpatterns = [
    # PlanoContas urls
    path('planos-contas/', views.PlanoContasListView.as_view(), name='listar_planos'),
    path('planos-contas/adicionar/', views.PlanoContasCreateView.as_view(), name='novo_plano'),
    path('planos-contas/atualizar/<int:pk>', views.PlanoContasUpdateView.as_view(), name='editar_plano'),
    path('planos-contas/detalhes/<int:pk>', views.PlanoContasDetailView.as_view(), name='detalhes_plano'),
    path('planos-contas/detelar/<int:pk>', views.PlanoContasDeleteView.as_view(), name='deletar_plano'),
    # PontosRecebimento urls
    path('pontos-recebimento/', views.PontoRecebimentoListView.as_view(), name='listar_pontos'),
    path('pontos-recebimento/adicionar', views.PontoRecebimentoCreateView.as_view(), name='novo_ponto'),
    path('pontos-recebimento/atualizar/<int:pk>', views.PontoRecebimentoUpdateView.as_view(), name='editar_ponto'),
    path('pontos-recebimento/detalhes/<int:pk>', views.PontoRecebimentoDetailViews.as_view(), name='detalhes_ponto'),
    path('pontos-recebimento/deletar/<int:pk>', views.PontoRecebimentoDeleteView.as_view(), name='deletar_ponto'),
    # Outras URLs
    path('cadastrar/funcionario', views.CadastrarFuncionario, name='cadastrar_funcionario'),
    path('cadastrar/plano-contas', views.CadastrarPlanoContas, name='cadastrar_plano_contas'),
    path('cadastrar/ponto-recebimento', views.CadastrarPontoRecebimento, name='cadastrar_ponto_recebimento'),
    path('cadastrar/caixa-lancamento', views.CaixaLancamento, name='caixa_lancamento'),
    path('cadastrar/caixa-repasse', views.CaixaRepasse, name='caixa_repasse'),
]