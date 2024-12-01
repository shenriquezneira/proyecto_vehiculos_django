from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Vehiculo
from .forms import VehiculoForm

def index(request):
    return render(request, 'vehiculo/index.html')

@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
@permission_required('vehiculo.add_vehiculomodel', raise_exception=True)
def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo/index')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/add.html', {'form': form})

@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def list_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    # Clasificación de precios
    for vehiculo in vehiculos:
        if vehiculo.precio <= 10000:
            vehiculo.condicion_precio = 'Bajo'
        elif 10000 < vehiculo.precio <= 30000:
            vehiculo.condicion_precio = 'Medio'
        else:
            vehiculo.condicion_precio = 'Alto'

    return render(request, 'vehiculo/list.html', {'vehiculos': vehiculos})
    return render(request, 'vehiculo/list.html', context)
