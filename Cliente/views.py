from django.shortcuts import render

# Create your views here.

def ConsultarCliente(request):
    return render(request,'cliente/consultar_cliente.html', context={})

def ListarClientes(request):

    from .models import Cliente

    clientes = Cliente.objects.all()

    context = {
        'clientes': clientes
    }

    return render(request, 'cliente/listar_cliente.html', context)