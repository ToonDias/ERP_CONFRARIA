from django.shortcuts import render

# Create your views here.

def CadastrarEmpresa(request):
    return render(request, 'financeiro/cadastrar_empresa.html', context={})

def CadastrarFuncionario(request):
    return render(request, 'financeiro/cadastrar_funcionario.html', context={})

def CadastrarPlanoContas(request):
    return render(request, 'financeiro/cadastrar_plano_contas.html', context={})

def CadastrarPontoRecebimento(request):
    return render(request, 'financeiro/cadastrar_ponto_receimento.html', context={})