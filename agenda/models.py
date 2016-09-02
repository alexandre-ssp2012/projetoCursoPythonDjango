from django.db import models

# Create your models here.

class ItemAgenda(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    descricao = models.TextField()
 

