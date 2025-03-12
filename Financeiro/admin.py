from django.contrib import admin

# Register your models here.

from .models import Pontorecebimento
from .models import Planocontas
from .models import Caixalancamento

class PontorecebimentoAdmin(admin.ModelAdmin):
    list_display = ['descricao']
    search_fields = ['descricao']
    actions = None

admin.site.register(Pontorecebimento, PontorecebimentoAdmin)

class PlanocontasAdmin(admin.ModelAdmin):
    list_display = ['codigo_financeiro','descricao',  'tipo']
    search_fields = ['descricao']
    actions = None

admin.site.register(Planocontas, PlanocontasAdmin)

class CaixalancamentoAdmin(admin.ModelAdmin):
    list_display = ['obs', 'plano_contas','operacao']
    search_fields = ['obs']
    actions = None

admin.site.register(Caixalancamento, CaixalancamentoAdmin)

