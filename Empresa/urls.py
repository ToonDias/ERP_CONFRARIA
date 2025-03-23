from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListarEmpresa.as_view(), name='listar_empresas'),
    path('adicionara/nova-empresa', views.CadastrarEmpresa.as_view(), name='nova_empresa'),
    path('atualizar/<int:pk>/', views.EditarEmpresa.as_view(), name='editar_empresa'),
    #path('empresa/editar', views.EditarEmpresa.as_view(), name='editar_empresa'),
    #path('empresa/deletar', views.DeletarEmpresa.as_view(), name='deletar_empresa'),
]