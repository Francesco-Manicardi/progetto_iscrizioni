from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Bambino(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    codice_fiscale = models.CharField(max_length=50, null=True)
    immagine = models.ImageField(null=True)

    def __str__(self):
        return f"{self.nome} {self.cognome}" 

    class Meta:
        verbose_name_plural = "Bambini"
