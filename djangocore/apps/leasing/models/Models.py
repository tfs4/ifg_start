from django.db import models
from django.contrib.auth.models import User


class ObjetoContrato(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo


class ContratoLocacao(models.Model):
    tipo = models.CharField(max_length=50)
    # locador = models.ForeignKey(
    #     'cadastro.Cliente',
    #     related_name="conta_cliente",
    #     on_delete=models.CASCADE,
    #     null=False,
    #     blank=False
    # )
    #
    # sub_locador = models.ForeignKey(
    #     'cadastro.Cliente',
    #     related_name="conta_sub_cliente",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True)
    #
    # empresa = models.ForeignKey(
    #     'cadastro.Empresa',
    #     on_delete=models.CASCADE,
    #     related_name='minha_empresa',
    #     blank=True, null=True
    # )
    #
    objeto_contrato = models.ForeignKey(ObjetoContrato, related_name='objetocontrato_contrato', on_delete=models.CASCADE )



class DadoContrato(models.Model):
    data_inicio_contrato = models.DateField()
    data_inicio_contabil = models.DateField()
    data_vencimento = models.DateField()
    taxa_incremental = models.FloatField()
    indice = models.CharField(max_length=10)
    contrato = models.ForeignKey(ContratoLocacao, related_name="contrato_dados", on_delete=models.CASCADE)


class PisCofinsRecuperar(models.Model):
    valor_pis = models.FloatField()
    valor_cofins = models.FloatField()
    contrato = models.ForeignKey(ContratoLocacao, related_name="contrato_pis", on_delete=models.CASCADE)


class SaldoInicial(models.Model):
    saldo_vpl = models.FloatField()
    base_calculo = models.FloatField()
    contrato = models.ForeignKey(ContratoLocacao, related_name="contrato_saldo", on_delete=models.CASCADE)


class CalculoVPL(models.Model):
    data_calculo = models.DateField()
    competencia = models.DateField()
    saldo_avp = models.FloatField()
    fluxo_pagamento_mensal = models.FloatField()
    avp = models.FloatField()
    saldo_devedor = models.FloatField()
    contrato = models.ForeignKey(ContratoLocacao, related_name="contrato_vpl", on_delete=models.CASCADE)

class DepreciacaoContrato(models.Model):
    data_calculo = models.DateField()
    competencia = models.DateField()
    valor_mensal_depreciacao = models.FloatField()
    contrato = models.ForeignKey(ContratoLocacao, related_name="contrato_depreciacao", on_delete=models.CASCADE)