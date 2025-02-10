from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from .forms import DiaryForm
from django.urls import reverse_lazy



class IndexView(TemplateView):
    template_name = 'index.html'


class DiaryCreateView(CreateView):
    template_name = 'diary_create.html'
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diary_create_complete')
