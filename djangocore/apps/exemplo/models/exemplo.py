from django.db import models


class ExemploModel(models.Model):
    nome = models.CharField(max_length=200)
    apelido = models.CharField(max_length=200)

