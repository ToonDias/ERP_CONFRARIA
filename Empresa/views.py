from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from .models import Empresa
from .forms import FormEmpresa
from django.urls import reverse_lazy

class ListarEmpresa(ListView):
    model = Empresa
    template_name = 'financeiro/empresa/empresa.html'
    context_object_name = 'empresas'

class CadastrarEmpresa(CreateView):
    model = Empresa
    form_class = FormEmpresa
    template_name = 'financeiro/empresa/empresa_cadastrar.html'
    success_url = reverse_lazy('listar_empresas')

class EditarEmpresa(UpdateView):
    model = Empresa
    form_class = FormEmpresa
    template_name = 'financeiro/empresa/empresa_editar.html'
    context_object_name = 'empresa'

    def get_success_url(self):
        return reverse_lazy('empresa_detalhes', kwargs={'empresa_id': self.object.id})