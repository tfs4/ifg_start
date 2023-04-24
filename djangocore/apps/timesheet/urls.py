# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'timesheet'
urlpatterns = [

    url(r'timesheet/lista/$', views.ListTimesheetView.as_view(), name='listatimesheet'),
    url(r'timesheet/adicionar/$', views.AdicionarTimesheetView.as_view(), name='adicionatimesheet'),
    url(r'timesheet/submeter/(?P<pk>[0-9]+)/$', views.SubmeterTimesheetView.as_view(), name='submetertimesheet'),





    url(r'timesheet/editar/(?P<pk>[0-9]+)/$', views.EditarTimesheetView.as_view(), name='editatimesheet'),
    url(r'timesheet/aprovar_submissao/$', views.AprovarTimesheetView.as_view(), name='aprovartimesheet'),
    url(r'timesheet/aprovar_submissao_horas/(?P<pk>[0-9]+)/$', views.AprovarHorasView.as_view(), name='aprovarhoras'),






]
