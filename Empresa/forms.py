from django import forms
from .models import Empresa

class FormEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'