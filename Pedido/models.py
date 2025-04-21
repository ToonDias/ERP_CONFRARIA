from django.db import models
from Cliente.models import ClientePessoa
from Estoque.models import Lote, LocalEstoque

# Create your models here.

class Pedido(models.Model):
    codigo = models.CharField(max_length=20)
    detalhes = models.TextField(max_length=254)
    data_cadastro = models.DateField('Data de cadastro', auto_now=True)
    data_entrega = models.DateField('Data de entrega')

    cliente = models.ForeignKey(ClientePessoa, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f'{self.codigo} - {self.cliente.nome}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    lote = models.ForeignKey(Lote, on_delete=models.PROTECT)
    local = models.ForeignKey(LocalEstoque, on_delete=models.PROTECT)
    quantidade = models.IntegerField()

    class Meta:
        verbose_name = 'Itens de pedido'
        verbose_name_plural = 'Itens de pedidos'
    
    def __str__(self):
        return f'Lote: {self.lote.codigo} - Produto: {self.lote.produto.descricao} - Quantidade: {self.quantidade}'

