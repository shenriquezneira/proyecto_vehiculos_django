from django.db import models

class Vehiculo(models.Model):
    CATEGORIAS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]

    MARCAS = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]

    marca = models.CharField(max_length=20, choices=MARCAS, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50, unique=True)
    serial_motor = models.CharField(max_length=50, unique=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='Particular')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ("visualizar_catalogo", "Puede Visualizar Catalogo"),
            ("add_vehiculomodel", "Puede Agregar Vehiculo"),
        ]

    def __str__(self):
        return f"{self.marca} {self.modelo}"
