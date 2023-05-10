# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from djangocore.apps.leasing.models import *

class DateInput(forms.DateInput):
    input_type = "date"
    def __init__(self, **kwargs):
        kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)

class ObjetoContratoForm(forms.ModelForm):

    class Meta:
        model = ObjetoContrato
        fields = ('tipo', )
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),


        }
        labels = {
            'tioo': _('Tipo'),
        }




'''
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
'''


class ContratoLocacaoForm(forms.ModelForm):

    class Meta:
        model = ContratoLocacao
        fields = ('numero',
                  'tipo', 'objeto_contrato','local_ativo', 'cpf_cnpj', 'data_inicio_contrato', 'data_fim_contrato',
                  'vigencia_primeiro_contrato', 'vigencia_aditivo_atual', 'clausula_renovacao', 'clausula_restritiva_de_uso',
                  'clausula_recisao_entra_partes', 'incentivos_recebidos', 'valor_incentivos')
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'objeto_contrato': forms.Select(attrs={'class': 'form-control select-produto'}),
            'local_ativo': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'cpf_cnpj': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'data_inicio_contrato' : DateInput(format=["%d-%m-%Y"], attrs={'class': 'form-control', 'size': '200'}),
            'data_fim_contrato': DateInput(format=["%d-%m-%Y"], attrs={'class': 'form-control', 'size': '200'}),
            'vigencia_primeiro_contrato': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'vigencia_aditivo_atual': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'clausula_renovacao': forms.Select(attrs={'class': 'form-control select-produto'}),
            'clausula_restritiva_de_uso': forms.Select(attrs={'class': 'form-control select-produto'}),
            'clausula_recisao_entra_partes': forms.Select(attrs={'class': 'form-control select-produto'}),
            'incentivos_recebidos': forms.Select(attrs={'class': 'form-control select-produto'}),
            'valor_incentivos' :  forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),


        }
        labels = {
            'tioo': _('Tipo'),
            'objeto_contrato':  _('Objeto do Contrato'),
        }



#ContratoLocacao