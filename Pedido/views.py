from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from .models import Pedido
from .models import ItemPedido

from .forms import FormPedido
from .forms import FormItemPedido

# Create your views here.

# Pedido Views
class PedidoListView(ListView):
    model = Pedido
    template_name = 'atendimento/pedido/list.html'
    context_object_name = 'pedidos'

class PedidoCreateView(CreateView):
    model = Pedido
    form_class = FormPedido
    template_name = 'atendimento/pedido/create.html'
    success_url = reverse_lazy('listar_pedidos')

class PedidoUpdateView(UpdateView):
    model = Pedido
    form_class = FormPedido
    template_name = 'atendimento/pedido/update.html'
    success_url = reverse_lazy('listar_pedidos')

class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'atendimento/pedido/details.html'
    context_object_name = 'pedido'

class PedidoDeleteView(DeleteView):
    model = Pedido
    template_name = 'atendmento/pedido/delete.html'
    success_url = reverse_lazy('listar_pedido')



def CadastrarPedido(request):
    return render(request, 'atendimento/cadastrar_pedido.html', context={})

def ConsultarPedido(request):
    return render(request, 'atendimento/consultar_pedido.html', context={})