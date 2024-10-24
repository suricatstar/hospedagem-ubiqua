from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View

from acomodacao.forms import UserForm
from acomodacao.models import Acomodacao

class IndexView(ListView):
    model = Acomodacao
    template_name = 'index.html'
    context_object_name = 'acomodacoes'

class LoginClienteView(CreateView):
    template_name = 'login.html'
    form_class = UserForm
    success_url = '/'