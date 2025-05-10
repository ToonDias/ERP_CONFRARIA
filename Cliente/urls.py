from django.urls import path
from . import views

urlpatterns = [
    # create views
    path('create/pf',views.PessoaFisicaCreateView.as_view(), name='pessoa_fisica_create'),
    path('create/pj',views.PessoaJuridicaCreateView.as_view(), name='pessoa_juridica_create'),
    # update views
    path('update/pf/<int:pk>',views.PessoaFisicaUpdateView.as_view(), name='pessoa_fisica_update'),
    path('update/pj/<int:pk>',views.PessoaJuridicaUpdateView.as_view(), name='pessoa_juridica_update'),
    # details views
    path('detail/pf/<int:pk>',views.PessoaFisicaDetailView.as_view(), name='pessoa_fisica_detail'),
    path('detail/pj/<int:pk>',views.PessoaJuridicaDetailView.as_view(), name='pessoa_juridica_detail'),
    # delete views
    path('delete/pf/<int:pk>',views.PessoaFisicaDeleteView.as_view(), name='pessoa_fisica_delete'),
    path('delete/pj/<int:pk>',views.PessoaJuridicaDeleteView.as_view(), name='pessoa_juridica_delete'),
    # search views
    path('search/pf', views.cliente_pf_search_view, name='pessoa_fisica_search'),
    path('search/pj', views.cliente_pj_search_view, name='pessoa_juridica_search'),
]