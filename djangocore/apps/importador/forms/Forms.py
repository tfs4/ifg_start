from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from djangocore.apps.importador.models import *




class ImportacaoForm(forms.ModelForm):

    class Meta:
        model = ImportacaoModel
        fields = ('tipo_relatorio', 'ano', 'estado','bimestre',)
        widgets = {

            'tipo_relatorio': forms.Select(attrs={'class': 'form-control select-produto'}),
            'ano': forms.Select(attrs={'class': 'form-control select-produto'}),
            'bimestre': forms.Select(attrs={'class': 'form-control select-produto'}),
            'estado': forms.Select(attrs={'class': 'form-control select-produto'}),

        }
        labels = {
            'tipo_relatorio': _('Tipo de importação'),
            'ano': _('Ano'),
            'bimestre': _('Bimestre'),
            'estado': _('Estado'),

        }
