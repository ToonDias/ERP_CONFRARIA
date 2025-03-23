from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from .models import Categoria
from .models import Produto

class ListarCategirias(ListView):
    model = Categoria
    template_name = 'estoque/listar_categorias.html'
    context_object_name = 'categorias'

class CadastrarProduto(ListView):
    model = Produto
    template_name = 'estoque/cadastrar_produto.html'
    context_object_name = 'produtos'

def CadastrarCategoria(request):
    from .models import Categoria

    categorias = Categoria.objects.all()

    context = {
        'categorias': categorias
    }

    return render(request, 'estoque/cadastrar_categoria.html', context)

def CadastrarFabricante(request):
    return render(request, 'estoque/cadastrar_fabricante.html', context={})

def CadastrarFornecedor(request):
    return render(request, 'estoque/cadastrar_fornecedor.html', context={})

def CadastrarUnidade(request):
    return render(request, 'estoque/cadastrar_unidade.html', context={})

def CadastrarLote(request):
    return render(request, 'estoque/cadastrar_lote.html', context={})

def CadastrarLocalEstoque(request):
    return render(request, 'estoque/cadastrar_local_estoque.html', context={})