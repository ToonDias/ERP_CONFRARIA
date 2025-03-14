# Generated by Django 5.1.6 on 2025-03-14 02:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Fabricante',
                'verbose_name_plural': 'Fabricantes',
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=65, verbose_name='Razão social')),
                ('nome_fantasia', models.CharField(max_length=65, verbose_name='Nome fantasia')),
                ('cpf_cnpj', models.CharField(max_length=17, verbose_name='CPF/CNPJ')),
                ('responsavel', models.CharField(max_length=100, verbose_name='Responsavel legal')),
                ('contato', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
            },
        ),
        migrations.CreateModel(
            name='LocalEstoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('ativo', models.BooleanField(default=True)),
                ('aviso_estoque', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Local de estoque',
                'verbose_name_plural': 'Locais de estoque',
            },
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Unidade',
                'verbose_name_plural': 'Unidades',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True, verbose_name='Codígo')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('detalhes', models.TextField(max_length=254)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Estoque.categoria')),
                ('fabricante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Estoque.fabricante')),
                ('unidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Estoque.unidade')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, verbose_name='Código')),
                ('custo', models.DecimalField(decimal_places=2, max_digits=6)),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço de venda')),
                ('quantidade', models.IntegerField()),
                ('data_vencimento', models.DateField(verbose_name='Data de vencimento')),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='Data de cadastro')),
                ('data_atualizacao', models.DateField(auto_now=True, verbose_name='Ultima modificação')),
                ('fornecedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Estoque.fornecedor')),
                ('produto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Estoque.produto')),
            ],
            options={
                'verbose_name': 'Lote',
                'verbose_name_plural': 'Lotes',
            },
        ),
    ]
