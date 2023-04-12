# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F



from datetime import datetime


class IndexView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        data_atual = datetime.now().date()

        context['data_atual'] = data_atual.strftime('%d/%m/%Y')

        return context


def handler404(request):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response


def handler500(request):
    response = render(request, '500.html', {})
    response.status_code = 500
    return response
