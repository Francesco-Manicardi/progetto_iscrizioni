from django.db import models
from centri.models import Centro
from datetime import datetime, timedelta

class Periodo(models.Model):
    nome = models.CharField(max_length=50)
    centri = models.ManyToManyField(Centro)
    inizio = models.DateField()
    fine = models.DateField()

    def __str__(self):
        return f"{self.nome} - da {self.inizio} a {self.fine}" 

    def get_days(self):
        ans = []
        cursor = self.inizio
        while(cursor <= self.fine):
            ans.append(len(ans))
            cursor = cursor + timedelta(days=1)
        
        return ans

    def get_nesima_data(self,i):
        return self.inizio + timedelta(days=i)

    class Meta:
        verbose_name_plural = "Periodi"
