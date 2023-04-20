# -*- coding: utf-8 -*-

from django.urls import reverse_lazy

from djangocore.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView
from django.shortcuts import redirect


from djangocore.apps.viagem.forms import *
from djangocore.apps.viagem.models import *


#### Tipos de Viagens
class ListTipoViagensView(CustomListView):
    template_name = 'viagem/list_tipo_viagem.html'
    model = TiposDeViagemModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listatiposviagens')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListTipoViagensView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Exemplo'
        context['add_url'] = reverse_lazy('viagem:adicionartiposviagens')
        return context

class AdicionarTipoViagemView(CustomCreateView):
    form_class = TipoViagemForm
    template_name = 'viagem/add.html'
    success_url = reverse_lazy('viagem:listatiposviagens')
    success_message = "Tipo de Viagem adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarTipoViagemView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR TIPO DE VIAGEM'
        context['return_url'] = reverse_lazy('viagem:listatiposviagens')
        return context

class EditarTipoViagemView(CustomUpdateView):
    form_class = TipoViagemForm
    model = TiposDeViagemModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listatiposviagens')
    success_message = "Tipo de Viagem Editado com Sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarTipoViagemView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('viagem:listatiposviagens')
        return context



#### Tipos de Solicitação
class ListTipoSolicitacaoView(CustomListView):
    template_name = 'viagem/list_tipo_solicitacao.html'
    model = TiposDeSolicitacaoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listatiposolicitacao')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListTipoSolicitacaoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Exemplo'
        context['add_url'] = reverse_lazy('viagem:adicionartiposolicitacao')
        return context

class AdicionarTipoSolicitacaoView(CustomCreateView):
    form_class = TipoDeSolicitacaoForm
    template_name = 'viagem/add.html'
    success_url = reverse_lazy('viagem:listatiposolicitacao')
    success_message = "Tipo de Solicitação adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarTipoSolicitacaoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR TIPO DE SOLICITAÇÃO'
        context['return_url'] = reverse_lazy('viagem:listatiposolicitacao')
        return context

class EditarTipoSolicitacaoView(CustomUpdateView):
    form_class = TipoDeSolicitacaoForm
    model = TiposDeSolicitacaoModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listatiposolicitacao')
    success_message = "Tipo de Solicitacao Editado com Sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarTipoSolicitacaoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('viagem:listatiposolicitacao')
        return context


#### Tipos de Transporte
class ListTipoTransporteView(CustomListView):
    template_name = 'viagem/list_tipo_transporte.html'
    model = TipoDeTransporteModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listatipotransporte')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListTipoTransporteView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Exemplo'
        context['add_url'] = reverse_lazy('viagem:adicionartipotransporte')
        return context

class AdicionarTipoTransporteView(CustomCreateView):
    form_class = TipoDeTransporteForm
    template_name = 'viagem/add.html'
    success_url = reverse_lazy('viagem:listatipotransporte')
    success_message = "Tipo de Transporte adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarTipoTransporteView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR TIPO DE TRANSPORTE'
        context['return_url'] = reverse_lazy('viagem:listatipotransporte')
        return context

class EditarTipoTransporteView(CustomUpdateView):
    form_class = TipoDeTransporteForm
    model = TipoDeTransporteModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listatipotransporte')
    success_message = "Tipo de Transporte Editado com Sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarTipoTransporteView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('viagem:listatipotransporte')
        return context



#### MotivosViagem
class ListMotivosView(CustomListView):
    template_name = 'viagem/list_motivo.html'
    model = MotivoDeViagemModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listamotivos')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListMotivosView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Motivos de Viagens'
        context['add_url'] = reverse_lazy('viagem:adicionarmotivo')
        return context

class AdicionarMotivoView(CustomCreateView):
    form_class = TipoMotivoForm
    template_name = 'viagem/add.html'
    success_url = reverse_lazy('viagem:listamotivos')
    success_message = "Motivo de Viagem adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarMotivoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR VIAGEM'
        context['return_url'] = reverse_lazy('viagem:listamotivos')
        return context

class EditarMotivoView(CustomUpdateView):
    form_class = TipoMotivoForm
    model = MotivoDeViagemModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listamotivos')
    success_message = "Motivo de Viagem Editada com Sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarMotivoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('viagem:listamotivos')
        return context



#### Viagem
class ListViagensView(CustomListView):
    template_name = 'viagem/list_viagens.html'
    model = ViagemModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listaviagem')
    permission_codename = 'solicitar_viagens'

    def get_queryset(self):
        #return self.model.objects.all()
        current_user = self.request.user
        viagens = []
        user_viagens = ViagemModel.objects.filter(solicitante=current_user)
        lambda viagens: ViagemModel.objects.filter(solicitante=current_user) or []

        return user_viagens

    def get_object(self):
        current_user = self.request.user
        return ViagemModel.objects.get(user=current_user)

    def get_context_data(self, **kwargs):
        context = super(ListViagensView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Viagens'
        context['add_url'] = reverse_lazy('viagem:adicionarviagem')
        return context

class AdicionarViagemView(CustomCreateView):
    form_class = ViagemForm
    template_name = 'viagem/add.html'
    success_url = reverse_lazy('viagem:listaviagem')
    success_message = "Tipo de Viagem adicionado com sucesso."
    permission_codename = 'solicitar_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def post(self, request, *args, **kwargs):


        self.object = None
        form_class = self.get_form_class()

        form = self.get_form(form_class)
        form.request_user = self.request.user

        if form.is_valid():
            self.object = form.save()
            return redirect(self.success_url)
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AdicionarViagemView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR VIAGEM'
        context['return_url'] = reverse_lazy('viagem:listaviagem')
        return context

class EditarViagemView(CustomUpdateView):
    form_class = ViagemForm
    model = ViagemModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listaviagem')
    success_message = "Viagem Editada com Sucesso."
    permission_codename = 'solicitar_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarViagemView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('viagem:listaviagem')
        return context