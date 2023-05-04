from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from djangocore.apps.timesheet.models.timesheet_model import HorasSemanais, Gastos
from decimal import Decimal


class HorasSemanaisForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(HorasSemanaisForm, self).__init__(*args, **kwargs)


    class Meta:
        model = HorasSemanais

# 'projeto'
        fields = ('semanas', 'hr_seg','hr_ter', 'hr_qua','hr_qui','hr_sex', 'hr_sab', 'hr_dom',  )

        widgets = {

            'semanas': forms.Select(attrs={'class': 'form-control'}),
            #'projeto': forms.Select(attrs={'class': 'form-control'}),

            'hr_seg': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control decimal-mask'}),
            'hr_ter': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control decimal-mask'}),
            'hr_qua': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control decimal-mask'}),
            'hr_qui': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control decimal-mask'}),
            'hr_sex': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control decimal-mask'}),
            'hr_sab': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control decimal-mask'}),
            'hr_dom': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control decimal-mask'}),

        }
        labels = {
            'horas': _('Horas Trabalhadas'),
            'semanas': _('Semana'),
            'hr_seg': _('Horas Trabalhadas na Segunda'),
            'hr_ter': _('Horas Trabalhadas na Terça'),
            'hr_qua': _('Horas Trabalhadas na Quarta'),
            'hr_qui': _('Horas Trabalhadas na Quinta'),
            'hr_sex': _('Horas Trabalhadas na Sexta'),
            'hr_sab': _('Horas Trabalhadas na Sabado'),
            'hr_dom': _('Horas Trabalhadas na Domingo'),
        }

    def save(self, commit=True):
        instance = super(HorasSemanaisForm, self).save(commit=False)
        instance.solicitante = self.request_user
        if commit:
            instance.save()
        return instance



class GastosForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(GastosForm, self).__init__(*args, **kwargs)


    class Meta:
        model = Gastos
        #
        # descricao = models.CharField(max_length=500, null=False, blank=False)
        # # projeto = models.ForeignKey('norli_projeto.ExemploModel', related_name="certificados_user", on_delete=models.CASCADE, null=True, blank=True)
        # solicitante = models.ForeignKey(User, related_name="gastos_user", on_delete=models.CASCADE, null=True,
        #                                 blank=True)
        # valor = models.CharField(max_length=10, null=False, blank=False)
        # file = models.FileField(upload_to='files/', null=False, blank=False)

        fields = ('descricao', 'valor','file',  )

        widgets = {

            #'projeto': forms.Select(attrs={'class': 'form-control'}),

            'descricao': forms.TextInput(attrs={'class': 'form-control', 'size': '500'}),
            'valor': forms.TextInput(attrs={'class': 'form-control', 'size': '500'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),


        }
        labels = {
            'descricao': _('Descrição'),
            'valor': _('Valor'),
            'file': _('Comprovante'),

        }

    def save(self, commit=True):
        instance = super(GastosForm, self).save(commit=False)
        instance.solicitante = self.request_user
        if commit:
            instance.save()
        return instance
