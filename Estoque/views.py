from django.shortcuts import render

# Create your views here.

def ExibirCategorias(request):
    from .models import Categoria

    categorias = Categoria.objects.all()

    context = {
        'categorias': categorias
    }

    return render(request, 'estoque/categorias.html', context)

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
    return render(request, 'estoque/cadastrar_fornecedor', context={})

def CadastrarUnidade(request):
    return render(request, 'estoque/cadastrar_unidade.html', context={})

def CadastrarProduto(request):
    return render(request, 'estoque/cadastrar_produto.html', contex={})

def CadastrarLote(request):
    return render(request, 'estoque/cadastrar_lote.html', context={})

def CadastrarLocalEstoque(request):
    return render(request, 'estoque/cadastrar_local_estoque.html', context={})