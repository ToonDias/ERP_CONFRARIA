from django.urls import path
from . import views

urlpatterns = [
    # create views
    path('create/F',views.PessoaFisicaCreateView.as_view(), name='pessoa_fisica_create'),
    path('create/J',views.PessoaJuridicaCreateView.as_view(), name='pssoa_juridica_create'),
    # update views
    path('update/F/<int:pk>',views.PessoaFisicaUpdateView.as_view(), name='pessoa_fisica_update'),
    path('update/J/<int:pk>',views.PessoaJuridicaUpdateView.as_view(), name='pssoa_juridica_update'),
    # details views
    path('detail/F/<int:pk>',views.PessoaFisicaDetailView.as_view(), name='pessoa_fisica_detail'),
    path('detail/J/<int:pk>',views.PessoaJuridicaDetailView.as_view(), name='pssoa_juridica_detail'),
    # delete views
    path('delete/F/<int:pk>',views.PessoaFisicaDeleteView.as_view(), name='pessoa_fisica_delete'),
    path('delete/J/<int:pk>',views.PessoaJuridicaDeleteView.as_view(), name='pssoa_juridica_delete'),
    # search views
    path('search/pf', views.cliente_pf_search_view, name='pessoa_fisica_search'),
    path('search/pf', views.cliente_pj_search_view, name='pessoa_juridica_search'),
]