from django.db import models
from django.db.models.deletion import CASCADE
from django.apps import apps


class Iscrizione(models.Model):
    nome = models.CharField(max_length=50)
    payed_at = models.DateField(null=True)
    bambino = models.ForeignKey("bambini.Bambino", on_delete=CASCADE)
    centro = models.ForeignKey("centri.Centro", on_delete=CASCADE)

    def get_prezzo_totale(self):
        return sum([conf.tariffa.prezzo for conf in self.get_configurazioni()])

    def __str__(self):
        return self.nome

    def get_periodi(self):
        return [conf.periodo for conf in self.get_configurazioni()]

    def get_configurazioni(self):
        return apps.get_model('configurazioni', 'Configurazione').objects.filter(iscrizione=self).all()

    class Meta:
        verbose_name_plural = "Iscrizioni"
