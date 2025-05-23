"""
URL configuration for Confraria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # URLS site
    path('', views.HomePage, name='home_page'),
    path('confraria/todos/', views.ItensAll, name='itens_all_page'),
    path('confraria/veganos/', views.ItensVeganos, name='itens_veganos_page'),
    path('confraria/zero-acucar/', views.ItensZeroAcucar, name='itens_zero_acucar_page'),
    path('confraria/zero-lactose/', views.ItensZeroLactose, name='itens_zero_lactose_page'),
    path('confraria/proteicos/', views.ItensProteicos, name='itens_proteicos_page'),
    path('confraria/drageados-snacks/', views.ItensDrageadosSnacks, name='itens_drageados_snacks_page'),
    path('confraria/evento/', views.ItensEvento, name='itens_eventos_page'),
    path('cliente/', views.ClientePage, name='cliente_page'),

    # outras URLS

    path('admin/', admin.site.urls),
    path('estoque/', include('Estoque.urls')),
    path('cliente/', include('Cliente.urls')),
    path('financeiro/', include('Financeiro.urls')),
    path('empresa/', include('Empresa.urls')),
    path('atendimento/', include('Pedido.urls')),
]

# Serve os arquivos de mídia enquanto estiver em desenvolvimento (quando DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)