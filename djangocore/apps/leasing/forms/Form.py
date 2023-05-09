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

