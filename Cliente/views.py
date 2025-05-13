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

from .forms import ClientePessoaFisicaFull
from .forms import EnderecoFormSet
from .forms import ContatoFormSet

# Create your views here.

# create view PF e PJ

class PessoaFisicaCreateView(CreateView):
    model = ClientePessoa
    form_class = FormClientePessoa
    template_name = 'cliente/pf/create.html'
    success_url = reverse_lazy('pessoa_fisica_search')

class PessoaJuridicaCreateView(CreateView):
    model = ClienteEmpresa
    form_class = FormClienteEmpresa
    template_name = 'cliente/pj/create.html'
    success_url = reverse_lazy('pessoa_juridica_search')

# update views PF e PJ

class PessoaFisicaUpdateView(UpdateView):
    model = ClientePessoa
    form_class = FormClientePessoa
    template_name = 'cliente/pf/update.html'
    context_object_name = 'cliente'
    success_url = reverse_lazy('pessoa_fisica_search')

class PessoaJuridicaUpdateView(UpdateView):
    model = ClienteEmpresa
    form_class = FormClienteEmpresa
    template_name = 'cliente/pj/update.html'
    context_object_name = 'cliente'
    success_url = reverse_lazy('pessoa_juridica_search')

# detail view PF e PJ

class PessoaFisicaDetailView(DetailView):
    model = ClientePessoa
    template_name = 'cliente/pf/details.html'
    context_object_name = 'cliente'

class PessoaJuridicaDetailView(DetailView):
    model = ClienteEmpresa
    template_name = 'cliente/pj/details.html'
    context_object_name = 'cliente'

# delete views PF e PJ

class PessoaFisicaDeleteView(DeleteView):
    model = ClientePessoa
    template_name = 'cliente/pf/delete.html'
    context_object_name = 'cliente'
    success_url = reverse_lazy('pessoa_fisica_search')

class PessoaJuridicaDeleteView(DeleteView):
    model = ClienteEmpresa
    template_name = 'cliente/pj/delete.html'
    context_object_name = 'cliente'
    success_url = reverse_lazy('pessoa_juridica_search')

# seach views PF e PJ

def cliente_pf_search_view(request):
    form = ClientePessoaFilterForm(request.GET or None)
    resultados = ClientePessoa.objects.all()

    if form.is_valid():
        nome = form.cleaned_data.get('nome')
        cpf_cnpj = form.cleaned_data.get('cpf_cnpj')
        obs = form.cleaned_data.get('obs')

        if nome:
            resultados = resultados.filter(nome__icontains=nome)
        if cpf_cnpj:
            resultados = resultados.filter(cpf_cnpj__icontains=cpf_cnpj)
        if obs:
            resultados = resultados.filter(obs__icontains=obs)

    return render(request, 'cliente/pf/serch_clientes.html', {
        'form': form,
        'resultados': resultados
    })

def cliente_pj_search_view(request):
    form = ClienteEmpresaFilterForm(request.GET or None)
    resultados = ClienteEmpresa.objects.all()

    if form.is_valid():
        nome = form.cleaned_data.get('nome')
        nome_fantasia = form.cleaned_data.get('nome_fantasia')
        cpf_cnpj = form.cleaned_data.get('cpf_cnpj')
        responsavel = form.cleaned_data.get('responsavel')
        responsavel_cpf = form.cleaned_data.get('responsavel_cpf')
        obs = form.cleaned_data.get('obs')

        if nome:
            resultados = resultados.filter(nome__icontains=nome)
        if nome_fantasia:
            resultados = resultados.filter(nome_fantasia__icontains=nome_fantasia)
        if cpf_cnpj:
            resultados = resultados.filter(cpf_cnpj__icontains=cpf_cnpj)
        if responsavel:
            resultados = resultados.filter(responsavel__icontains=responsavel)
        if responsavel_cpf:
            resultados = resultados.filter(responsavel_cpf__icontains=responsavel_cpf)
        if obs:
            resultados = resultados.filter(obs__icontains=obs)

    return render(request, 'cliente/pj/serch_clientes.html', {
        'form': form,
        'resultados': resultados
    })

def cliente_pf_create(request):
    if request.method == 'POST':
        cliente_form = ClientePessoaFisicaFull(request.POST)
        if cliente_form.is_valid():
            cliente = cliente_form.save(commit=False)
            endereco_formset = EnderecoFormSet(request.POST, instance=cliente)
            contato_formset = ContatoFormSet(request.POST, instance=cliente)
            if endereco_formset.is_valid() and contato_formset.is_valid():
                endereco_formset.save()
                contato_formset.save()
                return reverse_lazy('pessoa_fisica_search')
        
        else:
            cliente = None
            endereco_formset = EnderecoFormSet(request.POST)
            contato_formset = ContatoFormSet(request.POST)

    else:
        cliente_form = ClientePessoaFisicaFull()
        endereco_formset = EnderecoFormSet()
        contato_formset = ContatoFormSet()


    return render(request, 'cliente/pf/cliente_create.html', {
        'cliente_form': cliente_form,
        'endereco_formset': endereco_formset,
        'contato_formset': contato_formset,
    })