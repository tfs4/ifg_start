# -*- coding: utf-8 -*-

from django.urls import reverse_lazy

from djangocore.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView


from djangocore.apps.flavio.forms.Form import *
from djangocore.apps.flavio.models.Model import *

### Carro ###

class ListView(CustomListView):
    template_name = 'flavio/list.html' #'exemplo/exemplo_operacao/list.html'
    model = CarroModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('flavio:listaflavio')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Carro'
        context['add_url'] = reverse_lazy('flavio:adicionaflavio')
        return context
#
class AdicionarView(CustomCreateView):
    form_class = CarroForm
    template_name = 'flavio/add.html' #"exemplo/exemplo_operacao/add.html"
    success_url = reverse_lazy('flavio:listaflavio')
    success_message = "Adicionar Exemplo <b>%(cfop)s </b>adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR EXEMPLO'
        context['return_url'] = reverse_lazy('flavio:listaflavio')
        return context





class EditarView(CustomUpdateView):
    form_class = CarroForm
    model = CarroModel
   # template_name = "fiscal/natureza_operacao/natureza_operacao_edit.html"
    template_name = 'flavio/edit.html' #"exemplo/exemplo_operacao/edit.html"
    success_url = reverse_lazy('flavio:listaflavio')
    success_message = "Natureza da operação <b>%(cfop)s </b>editada com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarView,
                        self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy(
            'flavio:listaflavio')
        return context




### Pessoa ###

class ListPessoaView(CustomListView):
    template_name = 'flavio/list_pessoa.html'
    model = PessoaModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('flavio:lista_pessoa')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListPessoaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Pessoa'
        context['add_url'] = reverse_lazy('flavio:adiciona_pessoa')
        return context
#
class AdicionarPessoaView(CustomCreateView):
    form_class = PessoaForm
    template_name = 'flavio/add.html' #"exemplo/exemplo_operacao/add.html"
    success_url = reverse_lazy('flavio:lista_pessoa')
    success_message = "Adicionar Exemplo <b>%(cfop)s </b>adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarPessoaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR EXEMPLO'
        context['return_url'] = reverse_lazy('flavio:lista_pessoa')
        return context





class EditarPessoaView(CustomUpdateView):
    form_class = PessoaForm
    model = PessoaModel
    template_name = 'flavio/edit.html' #"exemplo/exemplo_operacao/edit.html"
    success_url = reverse_lazy('flavio:lista_pessoa')
    success_message = "Natureza da operação <b>%(cfop)s </b>editada com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarPessoaView,
                        self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy(
            'flavio:lista_pessoa')
        return context