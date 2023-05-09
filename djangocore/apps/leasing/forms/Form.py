# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from djangocore.apps.leasing.models import *



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




class ContratoLocacaoForm(forms.ModelForm):

    class Meta:
        model = ContratoLocacao
        fields = ('tipo', 'objeto_contrato', )
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'objeto_contrato': forms.Select(attrs={'class': 'form-control select-produto'}),


        }
        labels = {
            'tioo': _('Tipo'),
            'objeto_contrato':  _('Objeto do Contrato'),
        }



#ContratoLocacao