# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from djangocore.apps.viagem.models import *




class TipoViagemForm(forms.ModelForm):

    class Meta:
        model = TiposDeViagemModel
        fields = ('nome', )
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),

        }
        labels = {
            'nome': _('Nome'),
        }


class TipoDeSolicitacaoForm(forms.ModelForm):

    class Meta:
        model = TiposDeSolicitacaoModel
        fields = ('nome', )
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),

        }
        labels = {
            'nome': _('Nome'),
        }

class TipoDeTransporteForm(forms.ModelForm):

    class Meta:
        model = TipoDeTransporteModel
        fields = ('nome', )
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),

        }
        labels = {
            'nome': _('Nome'),
        }

class TipoMotivoForm(forms.ModelForm):

    class Meta:
        model = MotivoDeViagemModel
        fields = ('nome', )
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),

        }
        labels = {
            'nome': _('Nome'),
        }



class ViagemForm(forms.ModelForm):

    class Meta:
        model = ViagemModel
        fields = ('valor_passagem',
                  'dada_inicio',
                  'dada_fim',
                  'origem',
                  'destino',
                  'objetivo',
                  'tipo_viagem',
                  'tipo_solicitacao',
                  'motivo',
                  'tipo_transporte',    )
        widgets = {
            'valor_passagem': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'dada_inicio': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'dada_fim': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'origem': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'destino': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'objetivo': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'tipo_viagem': forms.Select(attrs={'class': 'form-control select-produto'}),
            'tipo_solicitacao': forms.Select(attrs={'class': 'form-control select-produto'}),
            'motivo': forms.Select(attrs={'class': 'form-control select-produto'}),
            'tipo_transporte': forms.Select(attrs={'class': 'form-control select-produto'}),
        }
        labels = {
            'valor_passagem': _('Valor da Passagem'),
            'dada_inicio': _('Data Inicio'),
            'dada_fim': _('Data Fim'),
            'origem': _('Origem'),
            'destino': _('Destino'),
            'objetivo': _('Objetivo'),
            'tipo_viagem': _('Tipo de Viagem'),
            'tipo_solicitacao': _('Tipo de Solicitação'),
            'motivo': _('Motivo'),
            'tipo_transporte': _('Tipo de Transporte'),

        }
