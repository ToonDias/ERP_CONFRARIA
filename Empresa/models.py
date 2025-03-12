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

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return f'{self.razao_social}({self.cnpj})'
