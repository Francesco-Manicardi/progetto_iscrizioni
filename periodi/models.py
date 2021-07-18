from django.db import models
from centri.models import Centro

class Periodo(models.Model):
    nome = models.CharField(max_length=50)
    centri = models.ManyToManyField(Centro)
    inizio = models.DateField()
    fine = models.DateField()

    def __str__(self):
        return f"{self.nome} - da {self.inizio} a {self.fine}" 

    class Meta:
        verbose_name_plural = "Periodi"
