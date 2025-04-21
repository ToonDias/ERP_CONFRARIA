from django import forms
from .models import Cliente

class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ClienteFilterForm(forms.Form):
    nome = forms.CharField(required=False, label="Nome")
    cpf_cnpj = forms.CharField(required=False, label="CPF/CNPJ")
    
    tipo_pessoa = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos')] + list(Cliente._meta.get_field('tipo_pessoa').choices),
        label="Tipo de Pessoa"
    )

    # data_nascimento = forms.DateField(
    #     required=False,
    #     label="Data de Nascimento",
    #     widget=forms.DateInput(attrs={'type': 'date'})
    # )