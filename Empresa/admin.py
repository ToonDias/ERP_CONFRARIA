from django.contrib import admin

# Register your models here.

from .models import Empresa
from .models import Empresaendereco
from .models import Empresacontato

class EmpresacontatoAdmin(admin.ModelAdmin):
    list_display = ['tipo_contato','contato', 'empresa']
    search_fields = ['contato']
    actions = None

admin.site.register(Empresacontato, EmpresacontatoAdmin)

class EmpresaenderecoAdim(admin.ModelAdmin):
    list_display = ['cep', 'endereco', 'numero', 'bairro', 'cidade', 'uf']
    search_fields = ['endereco', 'numero', 'bairro', 'cidade', 'uf']
    actions = None

admin.site.register(Empresaendereco, EmpresaenderecoAdim)

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['razao_social','cnpj']
    search_fields = ['razao_social','nome_fantasia','cnpj', 'responsavel', 'responsavel_cpf']
    actions = None

admin.site.register(Empresa, EmpresaAdmin)
