# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'flavio'
urlpatterns = [

    url(r'flavio/lista/$', views.ListView.as_view(), name='listaflavio'),
    url(r'flavio/adicionar/$', views.AdicionarView.as_view(), name='adicionaflavio'),
    url(r'flavio/editar/(?P<pk>[0-9]+)/$', views.EditarView.as_view(), name='editaflavio'),

    # Pessoa #
    url(r'flavio/lista_pessoa/$', views.ListPessoaView.as_view(), name='lista_pessoa'),
    url(r'flavio/adicionar_pessoa/$', views.AdicionarPessoaView.as_view(), name='adiciona_pessoa'),
    url(r'flavio/editar_pessoa/(?P<pk>[0-9]+)/$', views.EditarPessoaView.as_view(), name='edita_pessoa'),

]
