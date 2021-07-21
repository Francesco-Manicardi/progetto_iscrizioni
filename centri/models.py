from django.db import models
from django.apps import apps


class Centro(models.Model):
    nome = models.CharField(max_length=50)
    indirizzo = models.CharField(max_length=80)
    capienza = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

    def get_periodi(self):
        return apps.get_model('periodi', 'Periodo').objects.filter(centri__in=[self]).all()

    def get_tariffe(self):
        return apps.get_model('tariffe', 'Tariffa').objects.filter(centri__in=[self]).all()

    def get_iscrizioni(self):
        return apps.get_model('iscrizioni', 'Iscrizione').objects.filter(centro=self).all()

    def get_capienza_residua(self):
        return self.capienza - len(self.get_iscrizioni())

    class Meta:
        verbose_name_plural = "Centri"
