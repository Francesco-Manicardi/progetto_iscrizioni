from django.db import models
from django.db.models.deletion import CASCADE 
 

class Iscrizione(models.Model):
    nome = models.CharField(max_length=50)
    is_payed = models.BooleanField(default=False) 
    bambino = models.ForeignKey("bambini.Bambino", on_delete=CASCADE)

    def get_cost(self):
        pass
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Iscrizioni"