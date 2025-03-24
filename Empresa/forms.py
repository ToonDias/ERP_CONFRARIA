from django import forms
from .models import Empresa

class FormEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

    responsavel_data_nasc = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})  # Garantir que seja um campo de data HTML
    )