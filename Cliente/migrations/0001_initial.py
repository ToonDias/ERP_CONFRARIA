# Generated by Django 5.1.6 on 2025-03-11 02:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf_cnpj', models.CharField(max_length=18, verbose_name='CPF/CNPJ')),
                ('tipo_pessoa', models.CharField(choices=[('P', 'Pessoa física'), ('J', 'Pessoa jurídica')], max_length=1, verbose_name='Tipo de pessoa')),
                ('data_nascimento', models.DateField(blank=True, verbose_name='Data de nascimento')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contato', models.CharField(max_length=20)),
                ('obs', models.TextField(max_length=254, verbose_name='Observações')),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='Data de cadastro')),
                ('data_atualizacao', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('tipo_contato', models.CharField(choices=[('TR', 'Telefone residencial'), ('TC', 'Telefone comercial'), ('CR', 'Celular pessoaç'), ('CP', 'Celular comercial'), ('WP', 'WhatsApp'), ('IT', 'Instagram'), ('FB', 'Facebook'), ('OT', 'Outros')], max_length=2, verbose_name='Tipo de contato')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Cliente.cliente')),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('endereco', models.TextField(max_length=254, verbose_name='Endereço')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('bairro', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=20)),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('complemento', models.TextField(blank=True, max_length=254)),
                ('ponto_referencia', models.TextField(blank=True, max_length=254)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Cliente.cliente')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
    ]
