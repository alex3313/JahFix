# miApp/urls.py
from django.urls import path
from miApp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfilempleado/', views.perfilempleado, name='perfilempleado'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('historial/', views.historial, name='historial'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_empleado, name='registro'),
    path('reparaciones/<int:id>/detalle/', views.reparacion_detalle, name='reparacion_detalle'),
    path('seguimiento/', views.seguimiento, name='seguimiento'),
    path('cotizacion/', views.cotizacion, name='cotizacion'),
    path('cotizacionin/', views.cotizacionin, name='cotizacionin'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('condiciones/', views.condiciones_servicio, name='condiciones'),
    path('reparaciones/', views.lista_reparaciones, name='reparaciones'),
    path('reparaciones/<int:id>/notificacion/', views.notificacion, name='notificacion'),
    path('reparaciones/<int:id>/notificacioncli/', views.notificacioncli, name='notificacioncli'),
    path('recuperar/', auth_views.PasswordResetView.as_view(template_name='miApp/password_reset.html'), name='password_reset'),
    path('recuperar/done/', auth_views.PasswordResetDoneView.as_view(template_name='miApp/password_reset_done.html'), name='password_reset_done'),
    path('asignar/', views.asignar, name='asignar'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('reparaciones/<int:id>/reabrir', views.reabrir_reparacion, name='reabrir_reparacion'),
]
