from django.contrib import admin

# Register your models here.

from .models import Categoria
from .models import Fabricante
from .models import Unidade
from .models import Produto
from .models import Fornecedor
from .models import Lote
from .models import Local
from .models import Item

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['descricao']
    search_fields = ['descricao']
    actions = None

admin.site.register(Categoria, CategoriaAdmin)

class FabricanteAdmin(admin.ModelAdmin):
    list_display = ['descricao']
    search_fields = ['descricao']
    actions = None

admin.site.register(Fabricante, FabricanteAdmin)

class UnidadeAdmin(admin.ModelAdmin):
    list_display = ['descricao']
    search_fields = ['descricao']
    actions = None

admin.site.register(Unidade, UnidadeAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo','descricao','fabricante', 'categoria', 'unidade']
    search_fields = ['descricao']
    actions = None

admin.site.register(Produto, ProdutoAdmin)

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['razao_social','cpf_cnpj', 'responsavel']
    search_fields = ['razao_social']
    actions = None

admin.site.register(Fornecedor, FornecedorAdmin)

class LoteAdmin(admin.ModelAdmin):
    list_display = ['codigo','produto','produto__fabricante','quantidade','custo','preco_venda']
    search_fields = ['codigo']
    actions = None
   
admin.site.register(Lote, LoteAdmin)

class LocalAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'ativo', 'aviso_estoque']
    search_fields = ['descricao']
    actions = None

admin.site.register(Local, LocalAdmin)

class ItemAdim(admin.ModelAdmin):
    list_display = ['lote', 'local_origem', 'quantidade']
    actions = None

admin.site.register(Item, ItemAdim)