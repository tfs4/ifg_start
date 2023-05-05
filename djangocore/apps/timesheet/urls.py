# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'timesheet'
urlpatterns = [

    url(r'timesheet/lista/$', views.ListTimesheetView.as_view(), name='listatimesheet'),
    url(r'timesheet/adicionar/$', views.AdicionarTimesheetView.as_view(), name='adicionatimesheet'),
    url(r'timesheet/aprovar/$', views.AprovarTimesheetView.as_view(), name='aprovartimesheet'),

    url(r'timesheet/listargastos/$', views.ListGastosView.as_view(), name='listargastos'),
    url(r'timesheet/incluirgastos/$', views.AdicionarGastoView.as_view(), name='incluirgastos'),
    url(r'timesheet/aprovargastos/$', views.AprovarGastosView.as_view(), name='aprovargastos'),


]
