from django.shortcuts import render

def Site(request):
    return render(request,'confraria/index.html',context={})