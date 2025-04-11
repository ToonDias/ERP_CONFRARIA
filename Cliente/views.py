from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from .models import Cliente
from .forms import FormCliente

# Create your views here.

# Views Pessoa Fisica
class PessoaFisicaListView(ListView):
    model = Cliente
    template_name = 'cliente/pf/list.html'
    context_object_name = 'clientes'

class PessoaFisicaCreateView(CreateView):
    model = Cliente
    form_class = FormCliente
    template_name = 'cliente/pf/create.html'
    success_url = reverse_lazy('listar_pf')

class PessoaFisicaUpdadeViews(UpdateView):
    model = Cliente
    form_class = FormCliente
    template_name = 'cliente/pf/Update.html'
    success_url = reverse_lazy('listar_pf')

class PessoaFisicaDetailView(DetailView):
    model = Cliente
    template_name = 'cliente/pf/detail.html'
    context_object_name = 'cliente'

class PessoaFisicaDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente/pf/delete.html'
    success_url = reverse_lazy('listar_pf')

# Pessoa Juridica

class PessoaJuridicaListView(ListView):
    model = Cliente
    template_name = 'cliente/pj/list.html'
    context_object_name = 'clientes'

class PessoaJuridicaCreateView(CreateView):
    model = Cliente
    form_class = FormCliente
    template_name = 'cliente/pj/create.html'
    success_url = reverse_lazy('listar_pj')

class PessoaJuridicaUpdadeViews(UpdateView):
    model = Cliente
    form_class = FormCliente
    template_name = 'cliente/pj/Update.html'
    success_url = reverse_lazy('listar_pj')

class PessoaJuridicaDetailView(DetailView):
    model = Cliente
    template_name = 'cliente/pj/detail.html'
    context_object_name = 'cliente'

class PessoaJuridicaDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente/pj/delete.html'
    success_url = reverse_lazy('listar_pj')




def ConsultarCliente(request):
    return render(request,'cliente/consultar_clientes.html', context={})

def ListarClientes(request):

    from .models import Cliente

    clientes = Cliente.objects.all()

    context = {
        'clientes': clientes
    }

    return render(request, 'cliente/listar_pf.html', context={})

def CadastrarPessoaFisica(request):
    return render(request, 'cliente/pessoa_fisica.html', context={})

def CadastrarPessoaJuridica(request):
    return render(request, 'cliente/pessoa_juridica.html', context={})

def CadastrarPessoaFisicaEstrangeira(request):
    return render(request, 'cliente/pessoa_fisica_e.html', context={})

def CadastrarPessoaJuridicaEstrangeira(request):
    return render(request, 'cliente/pessoa_juridica_e.html', context={})