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

]
