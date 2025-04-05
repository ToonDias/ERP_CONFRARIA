from django import forms
from .models import Pedido
from .models import ItemPedido

class FormPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class FormItemPedido(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = '__all__'