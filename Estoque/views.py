from django.shortcuts import render

# Create your views here.

def ExibirCategorias(request):
    context = {
        'Categoria 1': 'valor 1',
        'Categoria 2':'valor 2'
    }

    render(request, 'categorias.html', context)