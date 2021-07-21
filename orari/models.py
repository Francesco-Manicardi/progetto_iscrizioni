from django.db import models


class Orario(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Orari"
