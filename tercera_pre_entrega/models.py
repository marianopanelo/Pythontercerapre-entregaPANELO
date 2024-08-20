from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=15) 
    apellido = models.CharField(max_length=15) 
    edad = models.IntegerField()
    telefono = models.IntegerField()
    direccion =  models.CharField(max_length=40)

class Reservas(models.Model):
    nombre = models.CharField(max_length=15)
    fecha_ingreso = models.DateField()
    noches_de_estadia = models.IntegerField()
    cabaña = models.CharField(max_length=40) 
    total_a_pagar = models.IntegerField()
    codigo_de_reserva = models.IntegerField()

class Comentarios(models.Model):
    nombre = models.CharField(max_length=25)
    cabaña_hospedado = models.CharField(max_length=25)
    dia_en_el_que_se_hospedo = models.DateField()
    comentario = models.CharField(max_length=450)