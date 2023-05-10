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
    #data_inicio_contrato
    #data_fim_contrato
    #vigencia_primeiro_contrato
    #vigencia_aditivo_atual
    #clausula_renovacao boolean
    #clausula_restritiva_de_uso boolean
    #clausula_recisao_entra_partes boolean
    #incentivos_recebidos boolean
    #valor_incentivos
