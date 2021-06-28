from django.db import models

# Create your models here.


class Bambino(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Bambini"
