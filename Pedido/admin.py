from django.contrib import admin

# Register your models here.

from .models import Pedido
from .models import ItemPedido

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['codigo','cliente__nome','data_cadastro','data_entrega']
    search_fields = ['codigo']
    actions = None

admin.site.register(Pedido, PedidoAdmin)


class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido__codigo','lote__produto__descricao','local__descricao','quantidade']
    search_fields = ['pedido__codigo','lote__produto__descricao','local__descricao']
    actions = None

admin.site.register(ItemPedido, ItemPedidoAdmin)