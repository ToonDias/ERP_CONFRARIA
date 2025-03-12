from django.db import models

# Create your models here.

class Categoria(models.Model):
    descricao = models.CharField('Descrição', max_length=50)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.descricao

class Fabricante(models.Model):
    descricao = models.CharField('Descrição', max_length=50)

    class Meta:
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'

    def __str__(self):
        return self.descricao

class Unidade(models.Model):
    descricao = models.CharField('Descrição', max_length=50)

    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'
    
    def __str__(self):
        return self.descricao


class Produto(models.Model):
    codigo = models.CharField('Codígo', max_length=20, unique=True)
    descricao = models.CharField('Descrição', max_length=50)
    detalhes = models.TextField(max_length=254)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.PROTECT)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.descricao}'
    
class Fornecedor(models.Model):
    razao_social = models.CharField('Razão social', max_length=65)
    nome_fantasia = models.CharField('Nome fantasia', max_length=65)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=17)
    responsavel = models.CharField('Responsavel legal', max_length=100)
    contato = models.CharField(max_length=20)
    email = models.EmailField('E-mail', max_length=50)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return f'{self.nome_fantasia} ({self.cpf_cnpj})' 

class Lote(models.Model):
    codigo = models.CharField('Código', max_length=20)
    custo = models.DecimalField(max_digits=6, decimal_places=2)
    preco_venda = models.DecimalField('Preço de venda', max_digits=6, decimal_places=2)
    quantidade = models.IntegerField()
    data_vencimento = models.DateField('Data de vencimento')
    data_cadastro = models.DateField('Data de cadastro', auto_now_add=True)
    data_atualizacao = models.DateField('Ultima modificação', auto_now=True)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, null=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'

    def __str__(self):
        return f'{self.codigo} : {self.produto.descricao}'

class Local(models.Model):
    descricao = models.CharField('Descrição', max_length=50)
    ativo = models.BooleanField(default=True)
    aviso_estoque = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Local de estoque'
        verbose_name_plural = 'Locais de estoque'

    def __str__(self):
        return self.descricao

class Item(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.PROTECT, null=True)
    local_origem = models.ForeignKey(Local, on_delete=models.PROTECT, null=True)
    quantidade = models.IntegerField()

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return f'Lote: {self.lote.codigo} - Produto: {self.lote.produto.descricao} - Quantidade: {self.quantidade}'