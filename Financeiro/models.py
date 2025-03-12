from django.db import models

# Create your models here.

#FORMA DE PAGAMENTO
# - DN - Dinheiro
# - PX - PIX
# - CC - Cartão de crédito
# - CD - Cartão de débito
# - TB - Transferência bancaria
# - OT - Outros

# FORMA DE RECEBIMENTO
# - Valor total
# - Valot parcial

# TIPO DE OPERAÇÃO
# - Entrada
# - Saída

# TIPO DE PLANO DE CONTAS
# - Receita
# - Dispesa

class Pontorecebimento(models.Model):
    descricao = models.CharField('Descrição', max_length=50)

    class Meta:
        verbose_name = 'Ponto de recebimento'
        verbose_name_plural = 'Pontos de recebimento'
    
    def __str__(self):
        return self.descricao

class Planocontas(models.Model):
    codigo_financeiro = models.CharField('Codigo financeiro',max_length=20)
    descricao = models.CharField('Descrição', max_length=50)
    tipo = models.CharField(max_length=1, choices=[('R','Receita'),('D','Dispesa')])

    class Meta:
        verbose_name = 'Plano de contas'
        verbose_name_plural = 'Planos de contas'
    
    def __str__(self):
        return f'{self.codigo_financeiro} : {self.descricao}'

class Caixalancamento(models.Model):
    operacao = models.CharField('Operação', max_length=1, choices=[('E','Entrada'),('S','Saída')])
    forma_recebimento = models.CharField('Forma de recebimento', max_length=2, choices=[('VT','Valor total'),('VP','Valor parcial')])
    forma_pagamento = models.CharField('Forma de pagamento', max_length=2,
                                       choices=[
                                           ('DN','Dinheiro'),
                                           ('PX','PIX'),
                                           ('CC','Cartão de crédito'),
                                           ('CD','Cartão de débito'),
                                           ('OT','Outros')
                                       ])
    ponto_recebimento = models.ForeignKey(Pontorecebimento, on_delete=models.PROTECT)
    plano_contas = models.ForeignKey(Planocontas, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    obs = models.TextField('Observação', max_length=254)
    data_pagamento = models.DateField()
    data_cadastro = models.DateField('Data de pagamento',auto_now_add=True)
    data_atualizacao = models.DateField('Data de atualização',auto_now=True)

    class Meta:
        verbose_name = 'Lançamento de caixa'
        verbose_name_plural = 'Lançamentos de caixa'
    
    def __str__(self):
        return f'{self.plano_contas} - R$: {self.valor}'