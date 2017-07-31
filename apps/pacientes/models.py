from django.db import models

# Create your models here.


class Paciente(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_registro = models.DateField()
    nombre_empresa = models.CharField(max_length=50)
    tipo_certificado = models.CharField(max_length=100)
    examenes_practicados = models.CharField(max_length=1000)
    telefono = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    estado_civil = models.CharField(max_length=50)
    escolaridad = models.CharField(max_length=50)
    profesion = models.CharField(max_length=100)
