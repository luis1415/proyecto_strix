from django import forms
from apps.pacientes.models import Paciente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'cedula',
            'nombre',
            'apellido',
            'fecha_registro',
            'nombre_empresa',
            'tipo_certificado',
            'examenes_practicados',
            'telefono',
            'celular',
            'ciudad',
            'fecha_nacimiento',
            'estado_civil',
            'escolaridad',
            'profesion',
        ]
        labels = {
            'cedula': 'Cedula',
            'nombre': 'Nombres',
            'apellido': 'Apellidos',
            'fecha_registro': 'Fecha Actual',
            'nombre_empresa': 'Nombre de la empresa',
            'tipo_certificado': 'Tipo de certificado',
            'examenes_practicados': 'Examenes practicados',
            'telefono': 'Telefono',
            'celular': 'Celular',
            'ciudad': 'Ciudad',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'estado_civil': 'Estado civil',
            'escolaridad': 'Escolaridad',
            'profesion': 'Profesion',
        }
        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_registro': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_certificado': forms.TextInput(attrs={'class': 'form-control'}),
            'examenes_practicados': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_civil': forms.TextInput(attrs={'class': 'form-control'}),
            'escolaridad': forms.TextInput(attrs={'class': 'form-control'}),
            'profesion': forms.Select(attrs={'class': 'form-control'}),
        }
