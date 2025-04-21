from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from .models import ClientePessoa
from .forms import FormClientePessoa
from .forms import ClientePessoaFilterForm

# Create your views here.

# Views Pessoa Fisica
class PessoaFisicaListView(ListView):
    model = ClientePessoa
    template_name = 'cliente/pf/list.html'
    context_object_name = 'clientes'

class PessoaFisicaCreateView(CreateView):
    model = ClientePessoa
    form_class = FormClientePessoa
    template_name = 'cliente/pf/create.html'
    success_url = reverse_lazy('listar_pf')

class PessoaFisicaUpdadeViews(UpdateView):
    model = ClientePessoa
    form_class = FormClientePessoa
    template_name = 'cliente/pf/Update.html'
    success_url = reverse_lazy('listar_pf')

class PessoaFisicaDetailView(DetailView):
    model = ClientePessoa
    template_name = 'cliente/pf/detail.html'
    context_object_name = 'cliente'

class PessoaFisicaDeleteView(DeleteView):
    model = ClientePessoa
    template_name = 'cliente/pf/delete.html'
    success_url = reverse_lazy('listar_pf')

# Pessoa Juridica

class PessoaJuridicaListView(ListView):
    model = ClientePessoa
    template_name = 'cliente/pj/list.html'
    context_object_name = 'clientes'

class PessoaJuridicaCreateView(CreateView):
    model = ClientePessoa
    form_class = FormClientePessoa
    template_name = 'cliente/pj/create.html'
    success_url = reverse_lazy('listar_pj')

class PessoaJuridicaUpdadeViews(UpdateView):
    model = ClientePessoa
    form_class = FormClientePessoa
    template_name = 'cliente/pj/Update.html'
    success_url = reverse_lazy('listar_pj')

class PessoaJuridicaDetailView(DetailView):
    model = ClientePessoa
    template_name = 'cliente/pj/detail.html'
    context_object_name = 'cliente'

class PessoaJuridicaDeleteView(DeleteView):
    model = ClientePessoa
    template_name = 'cliente/pj/delete.html'
    success_url = reverse_lazy('listar_pj')


# Seach views clientes

def cliente_search_view(request):
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

    return render(request, 'cliente/cliente/serch_clientes.html', {
        'form': form,
        'resultados': resultados
    })



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