# -*- coding: utf-8 -*-

from django.urls import reverse_lazy

from djangocore.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView
from django.shortcuts import redirect


from djangocore.apps.viagem.forms import *
from djangocore.apps.viagem.models import *
import random
import string




#### Tipos de Viagens
class ListTipoViagensView(CustomListView):
    template_name = 'viagem/list_tipo_viagem.html'
    model = TiposDeViagemModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listatiposviagens')
    permission_codename = 'cadastrar_item_viagens'

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
    permission_codename = 'cadastrar_item_viagens'

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
    permission_codename = 'cadastrar_item_viagens'

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
    permission_codename = 'cadastrar_item_viagens'

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
    permission_codename = 'cadastrar_item_viagens'

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
    permission_codename = 'cadastrar_item_viagens'

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
    permission_codename = 'cadastrar_item_viagens'

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
    permission_codename = 'cadastrar_item_viagens'

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
    permission_codename = 'cadastrar_item_viagens'

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
    permission_codename = 'cadastrar_item_viagens'

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
    permission_codename = 'cadastrar_item_viagens'

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
    permission_codename = 'cadastrar_item_viagens'

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
        user_viagens = ViagemModel.objects.filter(solicitante=current_user)

        return user_viagens

    def post(self, request, *args, **kwargs):
        if self.check_user_delete_permission(request, self.model):
            for key, value in request.POST.items():
                if value == "on":
                    instance = self.model.objects.get(id=key)
                    if not instance.autorizada and  not instance.homologada:
                        instance.delete()

        return redirect(self.success_url)

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



class ListAutorizarViagensView(CustomListView):
    template_name = 'viagem/list_all_viagens.html'
    model = ViagemModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listaautorizarviagem')
    permission_codename = 'autorizar_viagens'

    def get_queryset(self):
        # return self.model.objects.all()
        current_user = self.request.user
        user_viagens = ViagemModel.objects.filter(autorizada=False)

        return user_viagens
    # Remover items selecionados da database
    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
                if value == "on":
                    instance = self.model.objects.get(id=key)
                    instance.autorizada = True
                    instance.save()
        return redirect(self.success_url)



    def get_object(self):
        current_user = self.request.user
        return ViagemModel.objects.get(user=current_user)

    def get_context_data(self, **kwargs):
        context = super(ListAutorizarViagensView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Viagens'
        return context




class ListHomologarViagensView(CustomListView):
    template_name = 'viagem/list_homologar_viagens.html'
    model = ViagemModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listahomologacaoviagem')
    permission_codename = 'homologar_viagens'

    def get_queryset(self):
        # return self.model.objects.all()
        current_user = self.request.user
        user_viagens = ViagemModel.objects.filter(autorizada=True)
        user_viagens = user_viagens.filter(homologada=False)

        return user_viagens
    # Remover items selecionados da database
    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
                if value == "on":
                    instance = self.model.objects.get(id=key)
                    instance.homologada = True
                    instance.save()
        return redirect(self.success_url)



    def get_object(self):
        current_user = self.request.user
        return ViagemModel.objects.get(user=current_user)

    def get_context_data(self, **kwargs):
        context = super(ListHomologarViagensView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Viagens'
        return context




class PrestarContasView(CustomUpdateView):
    form_class = PrestacaoContaForm
    model = ViagemModel
    form_2 = ArquivosForm
    template_name = 'viagem/prestacao_de_contas.html'
    success_url = reverse_lazy('viagem:listaviagem')
    success_message = "Viagem Editada com Sucesso."
    permission_codename = 'solicitar_viagens'


    def post(self, request, *args, **kwargs):
        #arquivo = request.FILES['file']
        if request.FILES:
            self.object = None
            form = ArquivosForm(request.POST, request.FILES, instance=self.object)

            letters = string.ascii_lowercase
            name = ''.join(random.choice(letters) for i in range(20))
            nome_antigo = request.FILES['file'].name
            nome_antigo = nome_antigo.split('.')
            ext = nome_antigo[-1]

            if form.is_valid():
                request.FILES['file'].name = name + '.' + ext

                self.object = self.get_object()
                form.instance.viagem = ViagemModel.objects.get(pk=kwargs['pk'])
                self.object = form.save()
                return redirect(self.success_url)
            #return self.form_invalid(form)
        else:
            self.object = self.get_object()
            form_class = self.get_form_class()
            form = form_class(request.POST, instance=self.object)
            if form.is_valid():
                self.object = form.save()
                return redirect(self.success_url)
            return self.form_invalid(form)


    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(PrestarContasView, self).get_context_data(**kwargs)
        context['form_2'] = self.form_2
        context['return_url'] = reverse_lazy('viagem:listaviagem')
        #Arquivos.objects.get(pk=kwargs['pk'])
        #viagem = ViagemModel.objects.get(pk=kwargs['pk'])


        context['arquivos'] = Arquivos.objects.filter(viagem=context['object'])

        return context


#######################################################################################

class PrestarContasArquivosView(CustomUpdateView):
    form_class = PrestacaoContaForm
    model = ViagemModel
    form_2 = ArquivosForm
    template_name = 'viagem/prestacao_de_contas_arquivos.html'
    success_url = reverse_lazy('viagem:listaviagem')
    success_message = "Viagem Editada com Sucesso."
    permission_codename = 'solicitar_viagens'


    def post(self, request, *args, **kwargs):
        #arquivo = request.FILES['file']
        if request.FILES:
            self.object = None
            form = ArquivosForm(request.POST, request.FILES, instance=self.object)

            letters = string.ascii_lowercase
            name = ''.join(random.choice(letters) for i in range(20))
            nome_antigo = request.FILES['file'].name
            nome_antigo = nome_antigo.split('.')
            ext = nome_antigo[-1]

            if form.is_valid():
                request.FILES['file'].name = name + '.' + ext

                self.object = self.get_object()
                form.instance.viagem = ViagemModel.objects.get(pk=kwargs['pk'])
                self.object = form.save()
                return redirect(self.success_url)
            #return self.form_invalid(form)
        else:
            self.object = self.get_object()
            form_class = self.get_form_class()
            form = form_class(request.POST, instance=self.object)
            if form.is_valid():
                self.object = form.save()
                return redirect(self.success_url)
            return self.form_invalid(form)


    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(PrestarContasArquivosView, self).get_context_data(**kwargs)
        context['form_2'] = self.form_2
        context['return_url'] = reverse_lazy('viagem:listaviagem')



        context['arquivos'] = Arquivos.objects.filter(viagem=context['object'])

        return context

#######################################################################################


class EnviarArquivosView(CustomUpdateView):
    form_class = ArquivosForm
    model = ViagemModel
    form_2 = ArquivosForm
    template_name = 'viagem/enviar_arquivos.html'
    success_url = reverse_lazy('viagem:listaviagem')
    success_message = "Viagem Editada com Sucesso."
    permission_codename = 'solicitar_viagens'


    def post(self, request, *args, **kwargs):
        self.object = None
        form = ArquivosForm(request.POST, request.FILES, instance=self.object)

        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(20))
        nome_antigo = request.FILES['file'].name
        nome_antigo = nome_antigo.split('.')
        ext = nome_antigo[-1]

        if form.is_valid():
            request.FILES['file'].name = name + '.' + ext

            self.object = self.get_object()
            form.instance.viagem = ViagemModel.objects.get(pk=kwargs['pk'])
            self.object = form.save()
            return redirect(self.success_url)
        #return self.form_invalid(form)


    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EnviarArquivosView, self).get_context_data(**kwargs)
        context['form_2'] = self.form_2
        context['return_url'] = reverse_lazy('viagem:listaviagem')
        #Arquivos.objects.get(pk=kwargs['pk'])
        #viagem = ViagemModel.objects.get(pk=kwargs['pk'])


        context['arquivos'] = Arquivos.objects.filter(viagem=context['object'])

        return context



class ArquivosViagemView(CustomCreateView):
    form_class = ArquivosForm
    template_name = 'viagem/add_files.html'
    success_url = reverse_lazy('viagem:arquivosviagem')
    success_message = "Arquivos da Viagem"
    permission_codename = 'cadastrar_item_viagens'



    def get(self, request, *args, **kwargs):
        self.object = None
        obj = super().get(request, *args, **kwargs)
        # viagem = ViagemModel.objects.get(id=45)
        # # form_class = ArquivosForm(initial={'viagem': viagem})
        # obj.context_data['form'](initial={'viagem': viagem})

        # current_user = self.request.user
        # lviagems = ViagemModel.objects.get(id=45)
        # #lviagems = ViagemModel.objects.filter(solicitante=current_user)
        # valor = obj.context_data['form'].fields['viagem'] = lviagems
        return obj

    # def get_queryset(self):
    #     # # return self.model.objects.all()
    #     # current_user = self.request.user
    #     # user_viagens = ArquivosForm.objects.filter(autorizada=True)
    #     # user_viagens = user_viagens.filter(homologada=False)
    #     return self.model.objects.all()



    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def post(self, request, *args, **kwargs):
        self.object = None


        form = ArquivosForm(request.POST, request.FILES, instance=self.object)
        form.instance.viagem = ViagemModel.objects.get(pk=45)
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(20))
        nome_antigo = request.FILES['file'].name
        nome_antigo = nome_antigo.split('.')
        ext = nome_antigo[-1]

        if form.is_valid():
            request.FILES['file'].name = name+'.'+ext
            self.object = form.save()
            return redirect(self.success_url)
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(ArquivosViagemView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR ARQUIVOS'
        context['return_url'] = reverse_lazy('viagem:arquivosviagem')
        return context






















