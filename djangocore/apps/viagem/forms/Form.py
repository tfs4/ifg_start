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
