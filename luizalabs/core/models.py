from django.db import models


STATUS_CHOICES = (
    ('disponivel', 'DISPONIVEL'),
    ('indisponivel', 'INDISPONIVEL')
)


class Salas(models.Model):
    numero = models.IntegerField()
    capacidade = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    obs = models.CharField(max_length=200)
