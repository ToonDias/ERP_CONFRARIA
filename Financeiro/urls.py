from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/empresa', views.CadastrarEmpresa, name='cadastrar_empresa'),
    path('cadastrar/funcionario', views.CadastrarFuncionario, name='cadastrar_funcionario'),
    path('cadastrar/plano-contas', views.CadastrarPlanoContas, name='cadastrar_plano_contas'),
    path('cadastrar/ponto-recebimento', views.CadastrarPontoRecebimento, name='cadastrar_ponto_recebimento'),
    path('cadastrar/caixa-lancamento', views.CaixaLancamento, name='caixa_lancamento'),
    path('cadastrar/caixa-repasse', views.CaixaRepasse, name='caixa_repasse'),
]