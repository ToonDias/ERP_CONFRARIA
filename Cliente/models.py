from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)  # Obrigatório (Razão Social)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=17)  # Obrigatório
    tipo_pessoa = models.CharField('Tipo de pessoa', max_length=1, choices=[('F','Pessoa física'),('J','Pessoa jurídica')])

    class Meta:
        abstract = True

class ClientePessoa(Cliente):
    data_nascimento = models.DateField('Data de nascimento', blank=True, null=True)  # Opcional
    obs = models.TextField('Observações', max_length=254, blank=True)  # Opcional

    class Meta:
        verbose_name = 'Cliente pessoa física'
        verbose_name_plural = 'Clientes PF'

    def save(self, *args, **kwargs):
        self.tipo_pessoa = 'F'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nome} - {self.cpf_cnpj} - {self.tipo_pessoa}'
    
class ClienteEmpresa(Cliente):
    nome_fantasia = models.CharField('Nome fantasia', max_length=100)  # Obrigatório
    responsavel = models.CharField('Responsavel legal', max_length=100)  # Obrigatório

    responsavel_cpf = models.CharField('Responsavel legal CPF', max_length=17, blank=True)  # Opcional
    responsavel_data_nasc = models.DateField('Data de nascimento', blank=True, null=True)  # Opcional
    data_fundacao = models.DateField('Data de fundação', blank=True, null=True)  # Opcional
    obs = models.TextField('Observações', max_length=254, blank=True)  # Opcional

    class Meta:
        verbose_name = 'Cliente pessoa júridica'
        verbose_name_plural = 'Clientes PJ'

    def save(self, *args, **kwargs):
        self.tipo_pessoa = 'J'  # Define como pessoa física sempre
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nome} - {self.cpf_cnpj} - {self.tipo_pessoa}'
 
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
    
    cliente_pessoa = models.ForeignKey(ClientePessoa, on_delete=models.PROTECT, null=True, blank=True)
    cliente_empresa = models.ForeignKey(ClienteEmpresa, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return f'{self.tipo_contato} - {self.contato}'

class Endereco(models.Model):
    cep = models.CharField('CEP',max_length=9)
    endereco = models.CharField('Endereço', max_length=100)
    numero = models.IntegerField('Número')
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    uf = models.CharField('UF', max_length=2)
    complemento = models.TextField(max_length=254, blank=True)
    ponto_referencia = models.TextField(max_length=254, blank=True)
    
    cliente_pessoa = models.ForeignKey(ClientePessoa, on_delete=models.PROTECT, null=True, blank=True)
    cliente_empresa = models.ForeignKey(ClienteEmpresa, on_delete=models.PROTECT, null=True, blank=True)

    class Meta: 
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return f'{self.endereco} - {self.numero} - {self.bairro} - {self.cidade.upper()}/{self.uf.upper()}'