from django import forms
from .models import Categoria
from .models import Fabricante

class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
    
class FormFabricante(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = '__all__'
