from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View

class IndexView(TemplateView):
    template_name = 'index.html'