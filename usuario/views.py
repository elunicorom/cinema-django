# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Usuario
from forms import UsuarioForm
from django.views.generic import ListView,CreateView
from django.core.urlresolvers import reverse_lazy

def index(request):
    return render(request,'cinema/base.html')

class UsuarioList(ListView):
    model = Usuario
    template_name = 'usuario_list.html'

class UsuarioCreate(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario_create.html'
    success_url = reverse_lazy('usuario:listar')
