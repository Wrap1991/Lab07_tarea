from django.db import models

class Eventos(models.Model):
    nombre = models.CharField(max_length=255)  
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    celular = models.CharField(max_length=9)
    eventos = models.ForeignKey(Eventos, on_delete=models.CASCADE)  
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre