from django import forms
from .models import Categoria
from .models import Fabricante
from .models import Unidade
from .models import LocalEstoque

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

class FormLocalEstoque(forms.ModelForm):
    class Meta:
        model = LocalEstoque
        fields = '__all__'