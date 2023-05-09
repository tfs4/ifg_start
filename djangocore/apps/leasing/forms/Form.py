# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from djangocore.apps.leasing.models import *



class CarroForm(forms.ModelForm):

    class Meta:
        model = CarroModel
        fields = ('nome', 'placa', 'marca', 'pessoa')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'placa': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'pessoa': forms.Select(attrs={'class': 'form-control select-produto'}),



        }
        labels = {
            'nome': _('Nome'),
            'placa': _('Placa'),
            'marca': _('Marca'),
            'pessoa': _('Pessoa')
        }


class PessoaForm(forms.ModelForm):

    class Meta:
        model = PessoaModel
        fields = ('nome', 'cpf', 'endereco')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),



        }
        labels = {
            'nome': _('Nome Pessoa'),
            'cpf': _('CPF'),
            'endereco': _('Endereço'),
        }