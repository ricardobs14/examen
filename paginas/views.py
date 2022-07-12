import imp
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def paginaAdopcion(request):
    return render(request, 'paginas/paginaAdopcion.html')

def paginaAlimento(request):
    return render(request, 'paginas/paginaAlimento.html')

def paginaBandana(request):
    return render(request, 'paginas/paginaBandana.html')

def paginaCollar(request):
    return render(request, 'paginas/paginaCollar.html')

def paginaCorrea(request):
    return render(request, 'paginas/paginaCorrea.html')

def paginaIdentificaciones(request):
    return render(request, 'paginas/paginaIdentificaciones.html')

def paginaJuguete(request):
    return render(request, 'paginas/paginaJuguete.html')

def paginaRopa(request):
    return render(request, 'paginas/paginaRopa.html')