from time import timezone
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView

from diary.models import Diary,Todo

from .forms import DiaryForm,TodoForm
from django.urls import reverse_lazy

#diary
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['diary_list'] = Diary.objects.all() 
        context['todo_list'] = Todo.objects.all() 
        return context 
    
class DiaryCreateView(CreateView):
    template_name = 'diary/diary_create.html'
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diary_list') 


class DiaryListView(ListView):
    template_name = 'diary/diary_list.html'
    model = Diary

class DiaryDetailView(DetailView):
    template_name = 'diary/diary_detail.html'
    model = Diary



class DiaryUpdateView(UpdateView):
    template_name = 'diary/diary_update.html'
    model = Diary
    fields = ('date', 'title', 'text',)
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.save()
        return super().form_valid(form)
    
class DiaryDeleteView(DeleteView):
    template_name = 'diary/diary_delete.html'
    model = Diary
    success_url = reverse_lazy('diary:diary_list')


#todo
class TodoListView(ListView):
    template_name = 'todo/todo_list.html'
    model = Todo 
    context_object_name = 'todo_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TodoForm()
        return context 
    
    def post(self,request,*args,**kwargs):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diary:todo_list')
        return self.get(request, *args, **kwargs) 

    

class TodoDeleteView(DeleteView):
    template_name = 'todo/todo_delete.html'
    model = Todo
    success_url = reverse_lazy('diary:todo_list')

class TodoUpdateView(UpdateView):
    template_name = 'todo/todo_update.html'
    model = Todo
    fields = ('memo')
    success_url = reverse_lazy('diary:todo_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.save()
        return super().form_valid(form)