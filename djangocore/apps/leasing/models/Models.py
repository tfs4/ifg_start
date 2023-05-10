from django.db import models
from django.contrib.auth.models import User


class ObjetoContrato(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo




class TipoContrato(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo




class ContratoLocacao(models.Model):
    numero = models.CharField(max_length=200)
    tipo = models.ForeignKey(ObjetoContrato, related_name='tipo_contrato', on_delete=models.CASCADE )
    objeto_contrato = models.ForeignKey(ObjetoContrato, related_name='objetocontrato_contrato', on_delete=models.CASCADE )
    local_ativo = models.CharField(max_length=200)
    cpf_cnpj = models.CharField(max_length=200)
    data_inicio_contrato = models.DateField()
    data_fim_contrato = models.DateField()
    vigencia_primeiro_contrato = models.CharField(max_length=200)
    vigencia_aditivo_atual = models.CharField(max_length=200)
    clausula_renovacao = models.BooleanField(default=False)
    clausula_restritiva_de_uso  = models.BooleanField(default=False)
    clausula_recisao_entra_partes  = models.BooleanField(default=False)
    incentivos_recebidos  = models.BooleanField(default=False)
    valor_incentivos = models.CharField(max_length=200)
