from django.shortcuts import render

def HomePage(request):
    return render(request,'confraria/index.html',context={})

def ClientePage(request):
    return render(request, 'confraria/cliente.html', context={})

def ItensVeganos(request):
    return render(request, 'confraria/itens.html', context={})

def ItensZeroAcucar(request):
    return render(request, 'confraria/itens.html', context={})

def ItensZeroLactose(request):
    return render(request, 'confraria/itens.html', context={})

def ItensProteicos(request):
    return render(request, 'confraria/itens.html', context={})

def ItensDrageadosSnacks(request):
    return render(request, 'confraria/itens.html', context={})

def ItensEvento(request):
    return render(request, 'confraria/itens.html', context={})

def ItensAll(request):
    return render(request, 'confraria/itens.html', context={})