from django.db import models

# Create your models here.


class Centro(models.Model):
    nome = models.CharField(max_length=50)
    indirizzo = models.CharField(max_length=80)
    capienza = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Bambini"
