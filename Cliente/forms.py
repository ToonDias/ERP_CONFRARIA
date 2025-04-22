from django import forms
from .models import ClientePessoa
from .models import ClienteEmpresa

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
    
    tipo_pessoa = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos')] + list(ClientePessoa._meta.get_field('tipo_pessoa').choices),
        label="Tipo de Pessoa"
    )

    # data_nascimento = forms.DateField(
    #     required=False,
    #     label="Data de Nascimento",
    #     widget=forms.DateInput(attrs={'type': 'date'})
    # )

class ClienteEmpresaFilterForm(forms.Form):
    nome = forms.CharField(required=False, label='Razão Social')
    cpf_cnpj = forms.CharField(required=False, label='CNPJ')

    tipo_pessoa = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos')] + list(ClienteEmpresa._meta.get_field('tipo_pessoa').choices),
        label="Tipo de Pessoa"
    )

