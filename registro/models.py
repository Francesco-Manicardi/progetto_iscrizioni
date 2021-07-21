from django.db import models

# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE
from django.apps import apps


class Assenza(models.Model):
    bambino = models.ForeignKey("bambini.Bambino", on_delete=CASCADE)
    orario = models.ForeignKey("orari.Orario", on_delete=CASCADE)
    data = models.DateField()

    def __str__(self):
        return str(self.bambino)

    class Meta:
        verbose_name_plural = "Assenze"
