from django.shortcuts import render

# Create your views here.

def CadastrarPedido(request):
    return render(request, 'atendimento/cadastrar_pedido.html', context={})

def ConsultarPedido(request):
    return render(request, 'atendimento/consultar_pedido.html', context={})