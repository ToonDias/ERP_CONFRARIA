from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.ExibirCategorias, name='teste'),
]