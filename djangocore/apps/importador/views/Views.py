
from django.urls import reverse_lazy
from siconfipy import get_fiscal, get_budget, br_cods, get_annual_acc
from djangocore.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView

from datetime import timedelta, date, datetime
from djangocore.apps.importador.forms import *
from djangocore.apps.importador.models import *






class ListRGFView(CustomListView):
    template_name = 'RGF/list.html'
    model = RGFModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('importador:eac')
    permission_codename = 'rgf'

    def get_context_data(self, **kwargs):
        context = super(ListRGFView, self).get_context_data(**kwargs)
        context['title_complete'] = 'RGF'
        return context



class ListEACView(CustomListView):
    template_name = 'EAC/list.html'
    model = EACModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('importador:eac')
    permission_codename = 'eac'

    def get_context_data(self, **kwargs):
        context = super(ListEACView, self).get_context_data(**kwargs)
        context['title_complete'] = 'EAC'
        return context


class ListRREOView(CustomListView):
    template_name = 'RREO/list.html'
    model = RREOModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('importador:rreo')
    permission_codename = 'rreo'

    def get_context_data(self, **kwargs):
        context = super(ListRREOView, self).get_context_data(**kwargs)
        context['title_complete'] = 'RREO'
        return context




class ListImportacoesView(CustomListView):
    template_name = 'importador/list.html'
    model = ImportacaoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('importador:listimportacoes')
    permission_codename = 'importar_dados'

    def get_context_data(self, **kwargs):
        if self.check_user_permissions(self.request):
            context = super(ListImportacoesView, self).get_context_data(**kwargs)
            context['title_complete'] = 'Importações'
            context['add_url'] = reverse_lazy('importador:adicionaimportacao')
            return context




class AddImportacoesView(CustomListView):
    form_class = ImportacaoForm
    template_name = "importador/add.html"
    success_url = reverse_lazy('importador:listimportacoes')
    success_message = "Importar Dados"
    permission_codename = 'importar_dados'


    def import_rreo(self, ano, bimestre, estado):

        dados = get_budget(year=ano, period=bimestre, cod=estado)
        for index, row in dados.iterrows():
            relatorio = RREOModel.objects.create()
            relatorio.exercicio = row['exercicio']
            relatorio.demonstrativo = row['demonstrativo']
            relatorio.periodo = row['periodo']
            relatorio.periodicidade = row['periodicidade']
            relatorio.instituicao = row['instituicao']
            relatorio.cod_ibge = row['cod_ibge']
            relatorio.uf = row['uf']
            relatorio.anexo = row['populacao']
            relatorio.anexo = row['anexo']
            relatorio.esfera = row['esfera']
            relatorio.rotulo = row['rotulo']
            relatorio.coluna = row['coluna']
            relatorio.cod_conta = row['cod_conta']
            relatorio.conta = row['conta']
            relatorio.valor = row['valor']
            relatorio.importacao = self.object
            relatorio.save()

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.object = form.save()

        tipo_relatorio = request.POST['tipo_relatorio']
        ano = request.POST['ano']
        estado = request.POST['estado']
        bimestre = request.POST['bimestre']

#16:51


        if tipo_relatorio == 'RREO':
            estados = {12, 27, 16, 13, 29, 23, 53, 32, 52, 21, 51, 50, 31, 15, 25, 41, 26, 22, 24, 43, 33, 11, 14, 42,
                       35, 28, 17}



            startDate = datetime.datetime.strptime('2015-01-01', '%Y-%m-%d')
            endDate = datetime.datetime.strptime(str(date.today()), '%Y-%m-%d')
            for x in range(startDate.year, endDate.year):
                for y in range(1, 7):
                    print(x, y)
                    for key in estados:
                        self.import_rreo(x, y, key)

            month = date.today().month
            if month > 2:
                for key in estados:
                    self.import_rreo(endDate.year, 1, key)
            if month > 4:
                for key in estados:
                    self.import_rreo(endDate.year, 2, key)
            if month > 6:
                for key in estados:
                    self.import_rreo(endDate.year, 3, key)
            if month > 8:
                for key in estados:
                    self.import_rreo(endDate.year, 4, key)
            if month > 10:
                for key in estados:
                    self.import_rreo(endDate.year, 5, key)
            if month >= 12:
                for key in estados:
                    self.import_rreo(endDate.year, 6, key)

        return super(AddImportacoesView, self).post(request, form, *args, **kwargs)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AddImportacoesView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Importar Dados'
        context['return_url'] = reverse_lazy('importador:listimportacoes')
        return context




class EditImportacoesView(CustomUpdateView):
    form_class = ImportacaoForm
    model = ImportacaoModel

    template_name = "importador/edit.html"
    success_url = reverse_lazy('importador:listimportacoes')
    success_message = "Importação realizada com sucesso."
    permission_codename = 'importar_dados'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditImportacoesView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('importador:listimportacoes')
        return context