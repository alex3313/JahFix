from django.db import models
from django.contrib.auth.models import AbstractUser

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Empleado(AbstractUser):
    rol = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.username} ({self.rol})"

class Dispositivo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    descripcion = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.numero_serie})"

class Reparacion(models.Model):
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=50)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reparación {self.id} - {self.estado}"

class Etapa(models.Model):
    nombre_etapa = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_etapa

class DetalleEtapa(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    comentarios = models.TextField()
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    reparacion = models.ForeignKey(Reparacion, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.etapa.nombre_etapa} ({self.fecha_inicio} - {self.fecha_fin})"

class Notificacion(models.Model):
    mensaje = models.TextField()
    fecha_envio = models.DateField()
    estado = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    reparacion = models.ForeignKey(Reparacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Notificación a {self.cliente.nombre} - {self.estado}"

class Aprobacion(models.Model):
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    estado_aprobacion = models.CharField(max_length=50)
    fecha = models.DateField()
    reparacion = models.OneToOneField(Reparacion, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Aprobación {self.estado_aprobacion} - ${self.costo_estimado}"
