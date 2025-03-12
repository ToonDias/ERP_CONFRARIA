from django.contrib import admin

# Register your models here.

from .models import Contato
from .models import Endereco
from .models import Cliente

class ContatoAdmin(admin.ModelAdmin):
    list_display = ['tipo_contato','contato', 'cliente']
    search_fields = ['contato']
    actions = None

admin.site.register(Contato, ContatoAdmin)

class EnderecoAdim(admin.ModelAdmin):
    list_display = ['cep', 'endereco', 'numero', 'bairro', 'cidade', 'uf']
    search_fields = ['endereco', 'numero', 'bairro', 'cidade', 'uf']
    actions = None

admin.site.register(Endereco, EnderecoAdim)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome','cpf_cnpj','tipo_pessoa']
    search_fields = ['nome', 'cpf_cnpj']
    actions = None

admin.site.register(Cliente, ClienteAdmin)
