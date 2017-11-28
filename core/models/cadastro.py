from django.db import models

class Pessoa(models.Model):
    nome = models.CharField("Nome", max_length=50, blank=False)
    nascimento = models.DateField("Nascimento", blank=False)

    def __str__(self):
        return self.nome