from django import forms
from .models import PlanoContas

class FormPlanoContas(forms.ModelForm):
    class Meta:
        model = PlanoContas
        fields = '__all__'