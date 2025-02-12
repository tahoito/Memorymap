from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic import CreateView,DetailView

from diary.models import Diary

from .forms import DiaryForm
from django.urls import reverse_lazy



class IndexView(TemplateView):
    template_name = 'index.html'

class DiaryCreateView(CreateView):
    template_name = 'diary_create.html'
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diary_create_complete')

class DiaryCreateCompleteView(TemplateView):
    template_name = 'diary_create_complete.html'

class DiaryListView(ListView):
    template_name = 'diary_list.html'
    model = Diary

class DiaryDetailView(DetailView):
    template_name = 'diary_detail.html'
    model = Diary
