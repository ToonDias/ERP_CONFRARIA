from django.shortcuts import render

# Create your views here.

def ExibirCategorias(request):
    from .models import Categoria

    categorias = Categoria.objects.all()

    context = {
        'categorias': categorias
    }

    return render(request, 'estoque/categorias.html', context)