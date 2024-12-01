from django.contrib import admin
from django.contrib.auth.decorators import permission_required
from .models import Vehiculo

@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio', 'fecha_creacion')
