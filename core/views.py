from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def equipo(request):
    return render(request, 'core/equipo.html')

def login(request):
    return render(request, 'core/login.html')

def productos(request):
    return render(request, 'core/productos.html')

def recuperacion_de_contrasena(request):
    return render(request, 'core/recuperacion_de_contrasena.html')

def registro(request):
    return render(request, 'core/registro.html')  

from django. shortcuts import render
from .models import Auto


def auto(request):
    autos = Auto.objects.all()
    datos = {
        'autos': autos
    }
    return render(request, 'core/auto.html', datos)  

def form_auto(request):
    datos = {
        'form': AutoForm()
    }
    if request.method== 'POST':
        formulario = AutoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'core/form_auto.html',datos)  













 