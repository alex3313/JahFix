from django.contrib import admin
from .models import Cliente, Empleado, Dispositivo, Reparacion, Etapa, DetalleEtapa, Notificacion, Aprobacion

admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Dispositivo)
admin.site.register(Reparacion)
admin.site.register(Etapa)
admin.site.register(DetalleEtapa)
admin.site.register(Notificacion)
admin.site.register(Aprobacion)
