from django.db import models
from django.contrib.auth.models import User

class TiposDeViagemModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class TiposDeSolicitacaoModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class MotivoDeViagemModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class TipoDeTransporteModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class ViagemModel(models.Model):
    user = models.ForeignKey(User, related_name="viagem_user", on_delete=models.CASCADE, null=True, blank=True)
    valor_passagem = models.CharField(max_length=200)
    dada_inicio =  models.DateTimeField()
    dada_fim =  models.DateField()
    origem = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    objetivo = models.CharField(max_length=200)
    tipo_viagem         = models.ForeignKey(TiposDeViagemModel, related_name="viagem_tipo", on_delete=models.CASCADE)
    tipo_solicitacao    = models.ForeignKey(TiposDeViagemModel, related_name="viagem_solicitacao", on_delete=models.CASCADE)
    motivo              = models.ForeignKey(MotivoDeViagemModel, related_name="viagem_motivo", on_delete=models.CASCADE)
    tipo_transporte     = models.ForeignKey(TipoDeTransporteModel, related_name="viagem_transporte", on_delete=models.CASCADE)

