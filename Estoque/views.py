from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView

from .forms import FormCategoria

# Create your views here.
from .models import Categoria
from .models import Produto


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'estoque/categoria/list.html'
    context_object_name = 'categorias'
    
class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'estoque/categoria/create.html'
    form_class = FormCategoria
    template_name = 'estoque/categoria/create.html'
    success_url = reverse_lazy('listar_categorias')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'estoque/categoria/update.html'
    form_class = FormCategoria
    success_url = reverse_lazy('listar_categorias')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'estoque/categoria/delete.html'
    success_url = reverse_lazy('listar_categorias')

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'estoque/categoria/details.html'
    context_object_name = 'categoria'



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