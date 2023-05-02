# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'viagem'
urlpatterns = [

    # Tipo de Viagns
    url(r'viagem/listatipo/$', views.ListTipoViagensView.as_view(), name='listatiposviagens'),
    url(r'viagem/adicionartipo/$', views.AdicionarTipoViagemView.as_view(), name='adicionartiposviagens'),
    url(r'viagem/editartipo/(?P<pk>[0-9]+)/$', views.EditarTipoViagemView.as_view(), name='editartiposviagens'),

    # Tipo de Solicitação
    url(r'viagem/listatiposolicitacao/$', views.ListTipoSolicitacaoView.as_view(), name='listatiposolicitacao'),
    url(r'viagem/adicionartiposolicitacao/$', views.AdicionarTipoSolicitacaoView.as_view(), name='adicionartiposolicitacao'),
    url(r'viagem/editartiposolicitacao/(?P<pk>[0-9]+)/$', views.EditarTipoSolicitacaoView.as_view(), name='editartiposolicitacao'),

    # Tipo de Transporte
    url(r'viagem/listatipotransporte/$', views.ListTipoTransporteView.as_view(), name='listatipotransporte'),
    url(r'viagem/adicionartipotransporte/$', views.AdicionarTipoTransporteView.as_view(), name='adicionartipotransporte'),
    url(r'viagem/editartipotransporte/(?P<pk>[0-9]+)/$', views.EditarTipoTransporteView.as_view(),name='editartipotransporte'),

    # Motivos de Transporte
    url(r'viagem/listamotivos/$', views.ListMotivosView.as_view(), name='listamotivos'),
    url(r'viagem/adicionarmotivo/$', views.AdicionarMotivoView.as_view(), name='adicionarmotivo'),
    url(r'viagem/editarmotivo/(?P<pk>[0-9]+)/$', views.EditarMotivoView.as_view(), name='editarmotivo'),

    # Viagens
    url(r'viagem/listarviagem/$', views.ListViagensView.as_view(), name='listaviagem'),
    url(r'viagem/adicionarviagem/$', views.AdicionarViagemView.as_view(), name='adicionarviagem'),
    #url(r'viagem/editarviagem/(?P<pk>[0-9]+)/$', views.EditarViagemView.as_view(), name='editarviagem'),
    url(r'viagem/listarautorizarviagem/$', views.ListAutorizarViagensView.as_view(), name='listaautorizarviagem'),
    url(r'viagem/listarhomologarviagem/$', views.ListHomologarViagensView.as_view(), name='listahomologacaoviagem'),
    url(r'viagem/prestar_contas/(?P<pk>[0-9]+)/$', views.PrestarContasView.as_view(), name='prestar_contas'),
    url(r'viagem/prestar_contas_arquivos/(?P<pk>[0-9]+)/$', views.PrestarContasArquivosView.as_view(), name='prestar_contas_arquivos'),

    url(r'viagem/remover_arquivo/(?P<pk>[0-9]+)/(?P<viagem>[0-9]+)/$', views.RemoverArquivoView.as_view(), name='remover_arquivo'),

    url(r'viagem/enviar_arquivos/$', views.EnviarArquivosView.as_view(), name='enviar_arquivos'),
   # url(r'viagem/arquivosviagem/(?P<pk>[0-9]+)/$', views.ArquivosViagemView.as_view(), name='arquivosviagem'),
    url(r'viagem/arquivosviagem/$', views.ArquivosViagemView.as_view(), name='arquivosviagem'),

    url(r'viagem/listaraprovarpcviagem/$', views.ListAprovarPCViagensView.as_view(), name='listaaprovarpcviagem'),

    url(r'viagem/avaliar_prestacao_de_contas/(?P<pk>[0-9]+)/$', views.AvaliarPrestacaoDeContas.as_view(), name='avaliar_prestacao_de_contas'),
    url(r'viagem/avaliar_solicitacao_viagem/(?P<pk>[0-9]+)/$', views.AvaliarSolicitacaoViagem.as_view(), name='avaliar_solicitacao_viagem'),
    url(r'viagem/avaliar_arquivos/(?P<pk>[0-9]+)/$', views.AvaliarArquivosView.as_view(), name='avaliar_arquivos'),


]
