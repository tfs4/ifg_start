# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'leasing'
urlpatterns = [
    url(r'leasing/lista/$', views.ListObjContratoView.as_view(), name='listaobjcontrato'),
    url(r'leasing/adicionar/$', views.AdicionarObjContratoView.as_view(), name='adicionaobjcontrato'),
    url(r'leasing/editar/(?P<pk>[0-9]+)/$', views.EditarObjContratoView.as_view(), name='editarobjcontrato'),

    url(r'leasing/listacontradolocacao/$', views.ListContratoLocacaoView.as_view(), name='listacontratolocacao'),
    url(r'leasing/adicionarcontradolocacao/$', views.AdicionarContratoLocacaoView.as_view(), name='adicionacontratolocacao'),
    url(r'leasing/editarcontradolocacao/(?P<pk>[0-9]+)/$', views.EditarContratoLocacaoView.as_view(), name='editarcontratolocacao'),
]
