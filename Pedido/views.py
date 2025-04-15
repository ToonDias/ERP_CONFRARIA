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

# ItemPedido Views

class ItemPedidoListView(ListView):
    model = ItemPedido
    template_name = 'atendimento/item-pedido/list.html'
    context_object_name = 'itens-pedidos'

class ItemPedidoCreateView(CreateView):
    model = ItemPedido
    form_class = FormItemPedido
    template_name = 'atendimento/item-pedido/create.html'
    success_url = reverse_lazy('listar_itens')

class ItemPedidoUpdateView(UpdateView):
    model = ItemPedido
    form_class = FormItemPedido
    template_name = 'atendimento/item-pedido/update.html'
    success_url = reverse_lazy('listar_itens')

class ItemPedidoDetailView(DetailView):
    model = ItemPedido
    template_name = 'atendimento/item-pedido/details.html'
    context_object_name = 'item'

class ItemPedidoDeleteView(DeleteView):
    model = ItemPedido
    template_name = 'atendmento/item-pedido/delete.html'
    success_url = reverse_lazy('listar_itens')