from django.db import models 
 

class Iscrizione(models.Model):
    nome = models.CharField(max_length=50)
    is_payed = models.BooleanField() 

    def get_cost(self):
        pass
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Iscrizioni"