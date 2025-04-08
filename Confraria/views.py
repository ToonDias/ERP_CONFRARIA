from django.shortcuts import render

def homepage(request):
    return render(request,'confraria/index.html',context={})

def clientepage(request):
    return render(request, 'confraria/cliente.html', context={})