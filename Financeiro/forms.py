from django import forms
from .models import PlanoContas
from .models import PontoRecebimento

class FormPlanoContas(forms.ModelForm):
    class Meta:
        model = PlanoContas
        fields = '__all__'

class FormPontoRecebimento(forms.ModelForm):
    class Meta:
        mdoel = PontoRecebimento
        fields = '__all__'