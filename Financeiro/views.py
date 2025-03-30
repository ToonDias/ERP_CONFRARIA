from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from .models import PlanoContas
from .models import PontoRecebimento

from .forms import FormPlanoContas
from .forms import FormPontoRecebimento

# Create your views here.

# PlanoContas Views

class PlanoContasListView(ListView):
    model = PlanoContas
    template_name = 'financeiro/plano_contas/list.html'
    context_object_name = 'planoscontas'

class PlanoContasCreateView(CreateView):
    model = PlanoContas
    form_class = FormPlanoContas
    template_name = 'financeiro/plano_contas/create.html'
    success_url = reverse_lazy('listar_planos')

class PlanoContasUpdateView(UpdateView):
    model = PlanoContas
    form_class = FormPlanoContas
    template_name = 'financeiro/plano_contas/update.html'
    success_url = reverse_lazy('listar_planos')

class PlanoContasDetailView(DetailView):
    model = PlanoContas
    template_name = 'financeiro/plano_contas/details.html'
    context_object_name = 'plano'

class PlanoContasDeleteView(DeleteView):
    model = PlanoContas
    template_name = 'financeiro/plano_contas/delete.html'
    success_url = reverse_lazy('listar_planos')

# Ponto de recebimento Views

class PontoRecebimentoListView(ListView):
    model = PontoRecebimento
    template_name = 'financeiro/ponto_recebimento/list.html'
    context_object_name = 'pontos'

class PontoRecebimentoCreateView(CreateView):
    model = PontoRecebimento
    form_class = FormPontoRecebimento
    template_name = 'financeiro/ponto_recebimento/create.html'
    success_url = reverse_lazy('listar_pontos')

class PontoRecebimentoUpdateView(UpdateView):
    model = PontoRecebimento
    form_class = FormPontoRecebimento
    template_name = 'financeiro/ponto_recebimento/update.html'
    success_url = reverse_lazy('listar_pontos')

class PontoRecebimentoDetailViews(DetailView):
    model = PontoRecebimento
    template_name = 'financeiro/ponto_recebimento/details.html'
    context_object_name = 'ponto'

class PontoRecebimentoDeleteView(DeleteView):
    model = PontoRecebimento
    template_name = 'financeiro/ponto_recebimento/delete.html'
    success_url = reverse_lazy('listar_pontos')


def CadastrarFuncionario(request):
    return render(request, 'financeiro/cadastrar_funcionario.html', context={})

def CadastrarPlanoContas(request):
    return render(request, 'financeiro/cadastrar_plano_contas.html', context={})

def CadastrarPontoRecebimento(request):
    return render(request, 'financeiro/cadastrar_ponto_recebimento.html', context={})

def CaixaLancamento(request):
    return render(request, 'financeiro/caixa_lancamento.html', context={})

def CaixaRepasse(request):
    return render(request, 'financeiro/caixa_repasse.html', context={})