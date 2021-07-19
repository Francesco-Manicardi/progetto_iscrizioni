from django.db import models
from django.db.models.deletion import CASCADE


class Configurazione(models.Model):
    periodo = models.ForeignKey("periodi.Periodo", on_delete=CASCADE)
    tariffa = models.ForeignKey("tariffe.Tariffa", on_delete=CASCADE)
    iscrizione = models.ForeignKey("iscrizioni.Iscrizione", on_delete=CASCADE)

    def __str__(self):
        return f"{self.periodo} con tariffa  {self.tariffa}"

    class Meta:
        verbose_name_plural = "Configurazioni"
