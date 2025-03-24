from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListarEmpresa.as_view(), name='listar_empresas'),
    path('adicionara/nova-empresa', views.CadastrarEmpresa.as_view(), name='nova_empresa'),
    path('atualizar/<int:pk>/', views.EditarEmpresa.as_view(), name='editar_empresa'),
    path('detalhes/<int:pk>', views.DetalhesEmpresa.as_view(), name='detalhes_empresa'),
    path('empresa/<int:pk>/deletar/', views.DeletarEmpresa.as_view(), name='deletar_empresa'),
]