# Generated by Django 5.1.6 on 2025-03-12 02:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planocontas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_financeiro', models.CharField(max_length=20, verbose_name='Codigo financeiro')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('tipo', models.CharField(choices=[('R', 'Receita'), ('D', 'Dispesa')], max_length=1)),
            ],
            options={
                'verbose_name': 'Plano de contas',
                'verbose_name_plural': 'Planos de contas',
            },
        ),
        migrations.CreateModel(
            name='Pontorecebimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Ponto de recebimento',
                'verbose_name_plural': 'Pontos de recebimento',
            },
        ),
        migrations.CreateModel(
            name='Caixalancamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operacao', models.CharField(choices=[('E', 'Entrada'), ('S', 'Saída')], max_length=1, verbose_name='Operação')),
                ('forma_recebimento', models.CharField(choices=[('VT', 'Valor total'), ('VP', 'Valor parcial')], max_length=2, verbose_name='Forma de recebimento')),
                ('forma_pagamento', models.CharField(choices=[('DN', 'Dinheiro'), ('PX', 'PIX'), ('CC', 'Cartão de crédito'), ('CD', 'Cartão de débito'), ('OT', 'Outros')], max_length=2, verbose_name='Forma de pagamento')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('obs', models.TextField(max_length=254, verbose_name='Observação')),
                ('data_pagamento', models.DateField()),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='Data de pagamento')),
                ('data_atualizacao', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('plano_contas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Financeiro.planocontas')),
                ('ponto_recebimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Financeiro.pontorecebimento')),
            ],
            options={
                'verbose_name': 'Lançamento de caixa',
                'verbose_name_plural': 'Lançamentos de caixa',
            },
        ),
    ]
