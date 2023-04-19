from django.db import models


class TiposDeViagemModel(models.Model):
    nome = models.CharField(max_length=200)

class TiposDeSolicitacaoModel(models.Model):
    nome = models.CharField(max_length=200)

class MotivoDeViagemModel(models.Model):
    nome = models.CharField(max_length=200)

class TipoDeTransporteModel(models.Model):
    nome = models.CharField(max_length=200)


class ViagemModel(models.Model):
    valor_passagem = models.CharField(max_length=200)
    dada_inicio = models.CharField(max_length=200)
    dada_fim = models.CharField(max_length=200)
    origem = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    objetivo = models.CharField(max_length=200)

    tipo_viagem         = models.ForeignKey(TiposDeViagemModel, related_name="viagem_tipo", on_delete=models.CASCADE)
    tipo_solicitacao    = models.ForeignKey(TiposDeViagemModel, related_name="viagem_solicitacao", on_delete=models.CASCADE)
    motivo              = models.ForeignKey(MotivoDeViagemModel, related_name="viagem_motivo", on_delete=models.CASCADE)
    tipo_transporte     = models.ForeignKey(TipoDeTransporteModel, related_name="viagem_transporte", on_delete=models.CASCADE)

