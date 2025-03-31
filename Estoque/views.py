from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView

from .forms import FormCategoria
from .forms import FormFabricante
from .forms import FormUnidade
from .forms import FormLocalEstoque
from .forms import FormProduto
from .forms import FormLote

# Create your views here.
from .models import Categoria
from .models import Fabricante
from .models import Unidade
from .models import LocalEstoque
from .models import Produto
from .models import Lote


# Views Categoria
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'estoque/categoria/list.html'
    context_object_name = 'categorias'
    
class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'estoque/categoria/create.html'
    form_class = FormCategoria
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

# Views Fabricante

class FabricanteListView(ListView):
    model = Fabricante
    template_name = 'estoque/fabricante/list.html'
    context_object_name = 'fabricantes'

class FabricanteCreateView(CreateView):
    model = Fabricante
    template_name = 'estoque/fabricante/create.html'
    form_class = FormFabricante
    success_url = reverse_lazy('listar_fabricantes')

class FabricanteUpdateView(UpdateView):
    model = Fabricante
    template_name = 'estoque/fabricante/update.html'
    form_class = FormFabricante
    success_url = reverse_lazy('listar_fabricantes')

class FabricanteDetailView(DetailView):
    model = Fabricante
    template_name = 'estoque/fabricante/details.html'
    context_object_name = 'fabricante'

class FabricanteDeleteView(DeleteView):
    model = Fabricante
    template_name = 'estoque/fabricante/delete.html'
    success_url = reverse_lazy('listar_fabricantes')

# Views Unidade

class UnidadeListView(ListView):
    model = Unidade
    template_name = 'estoque/unidade/list.html'
    context_object_name = 'unidades'

class UnidadeCreateView(CreateView):
    model = Unidade
    form_class = FormUnidade
    template_name = 'estoque/unidade/create.html'
    success_url = reverse_lazy('listar_unidades')

class UnidadeUpdateView(UpdateView):
    model = Unidade
    form_class = FormUnidade
    template_name = 'estoque/unidade/update.html'
    success_url = reverse_lazy('listar_unidades')

class UnidadeDetailView(DetailView):
    model  = Unidade
    template_name = 'estoque/unidade/details.html'
    context_object_name = 'unidade'

class UnidadeDeleteView(DeleteView):
    model = Unidade
    template_name = 'estoque/unidade/delete.html'
    success_url = reverse_lazy('listar_unidades')

# Views LocalEstoque

class LocalEstoqueListView(ListView):
    model = LocalEstoque
    template_name = 'estoque/local_estoque/list.html'
    context_object_name = 'locais'

class LocalEstoqueCreateView(CreateView):
    model = LocalEstoque
    form_class = FormLocalEstoque
    template_name = 'estoque/local_estoque/create.html'
    success_url = reverse_lazy('listar_locais')

class LocalEstoqueUpdateView(UpdateView):
    model = LocalEstoque
    form_class = FormLocalEstoque
    template_name = 'estoque/local_estoque/update.html'
    success_url = reverse_lazy('listar_locais')

class LocalEstoqueDetailView(DetailView):
    model = LocalEstoque
    template_name = 'estoque/local_estoque/details.html'
    context_object_name = 'local'

class LocalEstoqueDeleteView(DeleteView):
    model = LocalEstoque
    template_name = 'estoque/local_estoque/delete.html'
    success_url = reverse_lazy('listar_locais')

#Views Produto

class ProdutoListView(ListView):
    model = Produto
    template_name = 'estoque/produto/list.html'
    context_object_name = 'produtos'

class ProdutoCreateViews(CreateView):
    model = Produto
    form_class = FormProduto
    template_name = 'estoque/produto/create.html'
    success_url = reverse_lazy('listar_produtos')

class ProdutoUpdateViews(UpdateView):
    model = Produto
    form_class = FormProduto
    template_name = 'estoque/produto/update.html'
    success_url = reverse_lazy('listar_produtos')

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'estoque/produto/details.html'
    context_object_name = 'produto'

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'estoque/produto/delete.html'
    success_url = reverse_lazy('listar_produtos')

# Views Lote

class LoteListView(ListView):
    model = Lote
    template_name = 'estoque/lote/list.html'
    context_object_name = 'lotes'

class LoteCreateView(CreateView):
    model = Lote
    form_class = FormLote
    template_name = 'estoque/lote/create.html'
    success_url = reverse_lazy('listar_lotes')

class LoteUpdateView(UpdateView):
    model = Lote
    form_class = FormLote
    template_name = 'estoque/lote/update.html'
    success_url = reverse_lazy('listar_lotes')

class LoteDetailView(DetailView):
    model = Lote
    template_name = 'estoque/lote/details.html'
    context_object_name = 'lote'

class LoteDeleteView(DeleteView):
    model = Lote
    template_name = 'estoque/lote/delete.html'
    success_url = reverse_lazy('listar_lotes')