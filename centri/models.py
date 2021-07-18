from django.db import models
from django.apps import apps
 

class Centro(models.Model):
    nome = models.CharField(max_length=50)
    indirizzo = models.CharField(max_length=80)
    capienza = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nome

    def get_periodi(self):
        return apps.get_model('periodi','Periodo').objects.filter(centri__in=[self]).all()

    def get_tariffe(self):
        return apps.get_model('tariffe','Tariffa').objects.filter(centri__in=[self]).all()

    class Meta:
        verbose_name_plural = "Centri"