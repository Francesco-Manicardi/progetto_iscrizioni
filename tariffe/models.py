from django.db import models

import sys
sys.path.append("..")

from centri.models import Centro
from orari.models import Orario

class Tariffa(models.Model):
    nome = models.CharField(max_length=50)
    centri = models.ManyToManyField(Centro)
    orari = models.ManyToManyField(Orario)
    prezzo = models.FloatField()

    def __str__(self):
        return f"{self.nome} - € {self.prezzo}" 
    
    class Meta:
        verbose_name_plural = "Tariffe"
