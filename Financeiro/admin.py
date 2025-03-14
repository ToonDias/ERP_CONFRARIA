from django.contrib import admin

# Register your models here.

from .models import PontoRecebimento
from .models import PlanoContas
from .models import CaixaLancamento

class PontoRecebimentoAdmin(admin.ModelAdmin):
    list_display = ['descricao']
    search_fields = ['descricao']
    actions = None

admin.site.register(PontoRecebimento, PontoRecebimentoAdmin)

class PlanoContasAdmin(admin.ModelAdmin):
    list_display = ['codigo_financeiro','descricao',  'tipo']
    search_fields = ['descricao']
    actions = None

admin.site.register(PlanoContas, PlanoContasAdmin)

class CaixaLancamentoAdmin(admin.ModelAdmin):
    list_display = ['obs', 'plano_contas','operacao']
    search_fields = ['obs']
    actions = None

admin.site.register(CaixaLancamento, CaixaLancamentoAdmin)

