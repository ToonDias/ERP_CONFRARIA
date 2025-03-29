from django import forms
from .models import Categoria
from .models import Fabricante
from .models import Unidade

class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
    
class FormFabricante(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = '__all__'

class FormUnidade(forms.ModelForm):
    class Meta:
        model = Unidade
        fields = '__all__'
