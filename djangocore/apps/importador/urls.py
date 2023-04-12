# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'importador'
urlpatterns = [

    url(r'importador/lista/$', views.ListImportacoesView.as_view(), name='listimportacoes'),
    url(r'importador/add/$', views.AddImportacoesView.as_view(), name='adicionaimportacao'),
    url(r'importador/edit/(?P<pk>[0-9]+)/$', views.EditImportacoesView.as_view(), name='editarimportacao'),

    url(r'importador/rreo/$', views.ListRREOView.as_view(), name='rreo'),
    url(r'importador/eac/$', views.ListEACView.as_view(), name='eac'),

    url(r'importador/rgf/$', views.ListRGFView.as_view(), name='rgf'),

]
