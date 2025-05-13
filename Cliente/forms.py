from django import forms
from django.forms import inlineformset_factory
from .models import ClientePessoa
from .models import ClienteEmpresa
from .models import Endereco
from .models import Contato


class FormClientePessoa(forms.ModelForm):
    class Meta:
        model = ClientePessoa
        exclude = ['tipo_pessoa']

class FormClienteEmpresa(forms.ModelForm):
    class Meta:
        model = ClienteEmpresa
        exclude = ['tipo_pessoa']

class ClientePessoaFilterForm(forms.Form):
    nome = forms.CharField(required=False, label="Nome")
    cpf_cnpj = forms.CharField(required=False, label="CPF")
    obs = forms.CharField(required=False, label='Observações')

    # data_nascimento = forms.DateField(
    #     required=False,
    #     label="Data de Nascimento",
    #     widget=forms.DateInput(attrs={'type': 'date'})
    # )

class ClienteEmpresaFilterForm(forms.Form):
    nome = forms.CharField(required=False, label='Razão Social')
    nome_fantasia = forms.CharField(required=False, label='Nome fantasia')
    cpf_cnpj = forms.CharField(required=False, label='CNPJ')
    responsavel = forms.CharField(required=False, label='Responsavel')
    responsavel_cpf = forms.CharField(required=False, label='Responsavel')
    obs = forms.CharField(required=False, label='Observações')


class ClientePessoaFisicaFull(forms.ModelForm):
    class Meta:
        model = ClientePessoa
        exclude =  ['tipo_pessoa'] 
    
EnderecoFormSet = inlineformset_factory(ClientePessoa, Endereco, fields='__all__', extra=1)
ContatoFormSet = inlineformset_factory(ClientePessoa, Contato, fields='__all__', extra=1)