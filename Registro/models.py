from django.db import models

class Perro(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=70)
    vacunas = models.IntegerField()

    def __str__(self):
        return self.nombre