from django.db import models

# Create your models here.

class Empresa(models.Model):
    razao_social = models.CharField('Razão social', max_length=65)
    nome_fantasia = models.CharField('Nome fantasia', max_length=65)
    cnpj = models.CharField('CPF/CNPJ', max_length=17)
    responsavel = models.CharField('Responsavel legal', max_length=100)
    responsavel_cpf = models.CharField('CPF', max_length=15)
    responsavel_data_nasc = models.DateField('Data de nascimento')
    contato = models.CharField(max_length=20)
    email = models.EmailField('E-mail', max_length=50)
    ativa = models.BooleanField('Ativa?',default=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return f'{self.razao_social}({self.cnpj})'
    

class EmpresaContato(models.Model):
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
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Empresa contato'
        verbose_name_plural = 'Empresa contatos'

    def __str__(self):
        return f'{self.empresa.razao_social} - {self.tipo_contato}'

class EmpresaEndereco(models.Model):
    cep = models.CharField('CEP',max_length=9)
    endereco = models.CharField('Endereço', max_length=100)
    numero = models.IntegerField('Número')
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    uf = models.CharField('UF', max_length=2)
    complemento = models.TextField(max_length=254, blank=True)
    ponto_referencia = models.TextField(max_length=254, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    class Meta: 
        verbose_name = 'Empresa endereço'
        verbose_name_plural = 'Empresa endereços'

    def __str__(self):
        return f'{self.endereco} - {self.numero} - {self.bairro} - {self.cidade.upper()}/{self.uf.upper()}'

