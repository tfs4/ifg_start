# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'timesheet'
urlpatterns = [

    url(r'timesheet/lista/$', views.ListTimesheetView.as_view(), name='listatimesheet'),
    url(r'timesheet/adicionar/$', views.AdicionarTimesheetView.as_view(), name='adicionatimesheet'),



]
