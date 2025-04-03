from django import forms
from .models import Categoria
from .models import Fabricante
from .models import Unidade
from .models import LocalEstoque
from .models import Produto
from .models import Lote
from .models import Fornecedor

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

class FormProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class FormLote(forms.ModelForm):
    class Meta:
        model = Lote
        fields = '__all__'

class FormFornecedor(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'