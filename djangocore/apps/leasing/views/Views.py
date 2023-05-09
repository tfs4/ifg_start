# -*- coding: utf-8 -*-

from django.urls import reverse_lazy

from djangocore.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView
from djangocore.apps.leasing.forms import *
from djangocore.apps.leasing.models import *





class ListObjContratoView(CustomListView):
    template_name = 'leasing/list.html'
    model = ObjetoContrato
    context_object_name = 'all_natops'
    success_url = reverse_lazy('leasing:listaobjcontrato')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListObjContratoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Carro'
        context['add_url'] = reverse_lazy('leasing:adicionaobjcontrato')
        return context

class AdicionarObjContratoView(CustomCreateView):
    form_class = ObjetoContratoForm
    template_name = 'leasing/add.html'
    success_url = reverse_lazy('leasing:listaobjcontrato')
    success_message = "Objeto do contrato adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarObjContratoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR OBJETO DO CONTRATO'
        context['return_url'] = reverse_lazy('leasing:listaobjcontrato')
        return context

class EditarObjContratoView(CustomUpdateView):
    form_class = ObjetoContratoForm
    model = ObjetoContrato
    template_name = 'leasing/edit.html'
    success_url = reverse_lazy('leasing:listaobjcontrato')
    success_message = "Objeto do contrado Editado com sucesso"
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarObjContratoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('leasing:listaobjcontrato')
        return context



