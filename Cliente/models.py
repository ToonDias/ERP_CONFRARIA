from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf_cnpj = models.CharField('CPF/CNPJ',max_length=18)
    tipo_pessoa =  models.CharField('Tipo de pessoa', max_length=1, choices=[('P','Pessoa física'),('J','Pessoa jurídica')])
    data_nascimento = models.DateField('Data de nascimento', blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.nome} - {self.cpf_cnpj}'
    
class Contato(models.Model):
    contato = models.CharField(max_length=20)
    obs = models.TextField('Observações', max_length=254, blank=True)
    data_cadastro = models.DateField('Data de cadastro', auto_now_add=True)
    data_atualizacao = models.DateField('Data de atualização', auto_now=True)
    tipo_contato = models.CharField('Tipo de contato', max_length=2,
                                    choices=[
                                        ('TR','Telefone residencial'),
                                        ('TC','Telefone comercial'),
                                        ('CP','Celular pessoal'),
                                        ('CC','Celular comercial'),
                                        ('WP','WhatsApp'),
                                        ('IT','Instagram'),
                                        ('FB','Facebook'),
                                        ('OT','Outros')
                                        ])
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return f'{self.cliente.nome} - {self.tipo_contato}'

class Endereco(models.Model):
    cep = models.CharField('CEP',max_length=9)
    endereco = models.CharField('Endereço', max_length=100)
    numero = models.IntegerField('Número')
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    uf = models.CharField('UF', max_length=2)
    complemento = models.TextField(max_length=254, blank=True)
    ponto_referencia = models.TextField(max_length=254, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    class Meta: 
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return f'{self.endereco} - {self.numero} - {self.bairro} - {self.cidade.upper()}/{self.uf.upper()}'
