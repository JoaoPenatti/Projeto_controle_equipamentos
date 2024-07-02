from django.db import models

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    material = models.TextField(max_length=255)
    data = models.DateField(null=False)
    sala = models.TextField(max_length=100)
 