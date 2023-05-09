# -*- coding: utf-8 -*-

from django.urls import reverse_lazy

from djangocore.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView
from django.shortcuts import redirect


from djangocore.apps.viagem.forms import *
from djangocore.apps.viagem.models import *
import random
import string


