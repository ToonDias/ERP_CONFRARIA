from django.shortcuts import render

# Create your views here.

def ConsultarCliente(request):
    return render(request,'cliente/consultar_clientes.html', context={})

def ListarClientes(request):

    from .models import Cliente

    clientes = Cliente.objects.all()

    context = {
        'clientes': clientes
    }

    return render(request, 'cliente/listar_clientes.html', context={})

def CadastrarPessoaFisica(request):
    return render(request, 'cliente/pessoa_fisica.html', context={})

def CadastrarPessoaJuridica(request):
    return render(request, 'cliente/pessoa_juridica.html', context={})

def CadastrarPessoaFisicaEstrangeira(request):
    return render(request, 'cliente/pessoa_fisica_e.html', context={})

def CadastrarPessoaJuridicaEstrangeira(request):
    return render(request, 'cliente/pessoa_juridica_e.html', context={})