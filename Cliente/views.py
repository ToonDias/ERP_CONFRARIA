from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from .models import ClientePessoa
from .models import ClienteEmpresa
from .forms import FormClientePessoa
from .forms import FormClienteEmpresa
from .forms import ClientePessoaFilterForm
from .forms import ClienteEmpresaFilterForm

# Create your views here.

# create view PF e PJ

class PessoaFisicaCreateView(CreateView):
    model = ClientePessoa
    form_class = FormClientePessoa
    template_name = 'cliente/pf/create.html'
    success_url = reverse_lazy('listar_pf')

class PessoaJuridicaCreateView(CreateView):
    model = ClienteEmpresa
    form_class = FormClienteEmpresa
    template_name = 'cliente/pj/create.html'
    success_url = reverse_lazy('listar_pj')

# update views PF e PJ

class PessoaFisicaUpdateView(UpdateView):
    model = ClientePessoa
    form_class = FormClientePessoa
    template_name = 'cliente/pf/Update.html'
    success_url = reverse_lazy('listar_pf')

class PessoaJuridicaUpdateView(UpdateView):
    model = ClienteEmpresa
    form_class = FormClienteEmpresa
    template_name = 'cliente/pj/Update.html'
    success_url = reverse_lazy('listar_pj')

# detail view PF e PJ

class PessoaFisicaDetailView(DetailView):
    model = ClientePessoa
    template_name = 'cliente/pf/detail.html'
    context_object_name = 'cliente'

class PessoaJuridicaDetailView(DetailView):
    model = ClienteEmpresa
    template_name = 'cliente/pf/detail.html'
    context_object_name = 'cliente'

# delete views PF e PJ

class PessoaFisicaDeleteView(DeleteView):
    model = ClientePessoa
    template_name = 'cliente/pf/delete.html'
    success_url = reverse_lazy('listar_pf')

class PessoaJuridicaDeleteView(DeleteView):
    model = ClienteEmpresa
    template_name = 'cliente/pj/delete.html'
    success_url = reverse_lazy('listar_pj')

# seach views PF e PJ

def cliente_pf_search_view(request):
    form = ClientePessoaFilterForm(request.GET or None)
    resultados = ClientePessoa.objects.all()

    if form.is_valid():
        nome = form.cleaned_data.get('nome')
        cpf_cnpj = form.cleaned_data.get('cpf_cnpj')
        tipo_pessoa = form.cleaned_data.get('tipo_pessoa')
        data_nascimento = form.cleaned_data.get('data_nascimento')

        if nome:
            resultados = resultados.filter(nome__icontains=nome)
        if cpf_cnpj:
            resultados = resultados.filter(cpf_cnpj__icontains=cpf_cnpj)
        if tipo_pessoa:
            resultados = resultados.filter(tipo_pessoa=tipo_pessoa)
        if data_nascimento:
            resultados = resultados.filter(data_nascimento=data_nascimento)

    return render(request, 'cliente/pf/serch_clientes.html', {
        'form': form,
        'resultados': resultados
    })

def cliente_pj_search_view(request):
    form = ClientePessoaFilterForm(request.GET or None)
    resultados = ClientePessoa.objects.all()

    if form.is_valid():
        nome = form.cleaned_data.get('nome')
        cpf_cnpj = form.cleaned_data.get('cpf_cnpj')
        tipo_pessoa = form.cleaned_data.get('tipo_pessoa')
        data_nascimento = form.cleaned_data.get('data_nascimento')

        if nome:
            resultados = resultados.filter(nome__icontains=nome)
        if cpf_cnpj:
            resultados = resultados.filter(cpf_cnpj__icontains=cpf_cnpj)
        if tipo_pessoa:
            resultados = resultados.filter(tipo_pessoa=tipo_pessoa)
        if data_nascimento:
            resultados = resultados.filter(data_nascimento=data_nascimento)

    return render(request, 'cliente/pj/serch_clientes.html', {
        'form': form,
        'resultados': resultados
    })