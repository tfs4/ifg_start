from django.db import models


class TiposDeViagemModel(models.Model):
    nome = models.CharField(max_length=200)

class TiposDeSolicitacaoModel(models.Model):
    nome = models.CharField(max_length=200)

class MotivoDeViagemModel(models.Model):
    nome = models.CharField(max_length=200)

class TipoDeTransporteModel(models.Model):
    nome = models.CharField(max_length=200)



# valor da passagem, origem, destino
# data inicio, data de fim
# objetivo da viagem