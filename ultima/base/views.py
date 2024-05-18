from django.shortcuts import render

from base.forms import Contatoforms
from base.forms import Reservaforms


# View inicio, que é a primeira a ser acessada pelo usuário
def inicio(request):
    return render(request, 'inicio.html')


# View contato

def contato(request):
    formulario = Contatoforms()
    contexto = {
        'formulario':formulario
        }
    
    return render(request,'contato.html',contexto)

# View Reserva

def reserva(request):
    formulario = Reservaforms()
    contexto = {
        'formulario': formulario
    }
    return render (request, 'reserva.html', contexto)