# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from djangocore.apps.exemplo.models import ExemploModel




class ExemploForm(forms.ModelForm):

    class Meta:
        model = ExemploModel
        fields = ('nome', 'apelido')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '50'}),
            'apelido': forms.TextInput(attrs={'class': 'form-control', 'size': '50'}),



        }
        labels = {
            'nome': _('Nome'),
            'apelido': _('Apelido'),
        }
