# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Empleado
from .models import Reparacion

from .models import DetalleEtapa

class DetalleEtapaForm(forms.ModelForm):
    class Meta:
        model = DetalleEtapa
        fields = ['fecha_inicio', 'fecha_fin', 'comentarios', 'etapa']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
            'comentarios': forms.Textarea(attrs={'rows': 3}),
        }

class EmpleadoRegistroForm(UserCreationForm):
    class Meta:
        model = Empleado
        fields = ['username', 'email', 'first_name', 'last_name', 'rol', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'rol': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rol'}),  # ← corregido aquí
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'}),
        }

class EmpleadoLoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Ingresa tu nombre de usuario'
    }))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Ingresa tu contraseña'
    }))


class ReparacionForm(forms.ModelForm):
    class Meta:
        model = Reparacion
        fields = ['fecha_ingreso', 'estado', 'dispositivo', 'empleado']
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
        }
