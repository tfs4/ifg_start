# -*- coding: utf-8 -*-

from django.urls import reverse_lazy

from djangocore.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView


from djangocore.apps.exemplo.forms.FormExemplo import ExemploForm
from djangocore.apps.exemplo.models.exemplo import ExemploModel



class ListView(CustomListView):
    template_name = 'exemplo/exemplo_operacao/list.html'
    model = ExemploModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('exemplo:listaexemplo')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Exemplo'
        context['add_url'] = reverse_lazy('exemplo:adicionaexemplo')
        return context

class AdicionarView(CustomCreateView):
    #form_class = NaturezaOperacaoForm
    form_class = ExemploForm
    template_name = "exemplo/exemplo_operacao/add.html"
    success_url = reverse_lazy('exemplo:listaexemplo')
    success_message = "Adicionar Exemplo <b>%(cfop)s </b>adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR EXEMPLO'
        context['return_url'] = reverse_lazy('exemplo:listaexemplo')
        return context





class EditarView(CustomUpdateView):
    print('Ok')
    form_class = ExemploForm
    model = ExemploModel
   # template_name = "fiscal/natureza_operacao/natureza_operacao_edit.html"
    template_name = "exemplo/exemplo_operacao/edit.html"
    success_url = reverse_lazy('exemplo:listaexemplo')
    success_message = "Natureza da operação <b>%(cfop)s </b>editada com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarView,
                        self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy(
            'exemplo:listaexemplo')
        return context
