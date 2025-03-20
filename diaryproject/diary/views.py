from time import timezone
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView
from django.http import JsonResponse


from diary.models import Diary,Todo,Tag
import uuid 
from django.db.models import Q

from .forms import DiaryForm,TodoForm
from django.urls import reverse_lazy

#diary
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['diary_list'] = Diary.objects.all().order_by('-id')
        context['todo_list'] = Todo.objects.all().order_by('-id') 
        return context 

class DiaryCreateView(CreateView):
    template_name = 'diary/diary_create.html'
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diary_list') 

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.save()

        # タグ処理
        tag_names = form.cleaned_data["tags"].split()
        for tag_name in tag_names:
            if tag_name.startswith("#"):
                tag, created = Tag.objects.get_or_create(name=tag_name[1:])
                diary.tags.add(tag)

        return redirect('diary:diary_list')


class DiaryListView(ListView):
    template_name = 'diary/diary_list.html'
    model = Diary
    queryset = Diary.objects.all().order_by('-id')

    def get_queryset(self):
        query = self.request.GET.get('q', '')

        if query.startswith("#"):  # ハッシュタグ検索
            tag_name = query[1:]
            return Diary.objects.filter(tags__name__icontains=tag_name).order_by('-id')
        elif query:  # タイトル & 本文のキーワード検索
            return Diary.objects.filter(Q(title__icontains=query) | Q(text__icontains=query)).order_by('-id')
        else:  # すべての日記
            return Diary.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DiaryForm()  # 日記の新規作成フォーム
        return context
    

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

        # タグの更新
        diary.tags.clear()  # 既存のタグをリセット
        tag_names = form.cleaned_data["tags"].split()
        for tag_name in tag_names:
            if tag_name.startswith("#"):
                tag, created = Tag.objects.get_or_create(name=tag_name[1:])
                diary.tags.add(tag)

        return super().form_valid(form)
    
class DiaryDeleteView(DeleteView):
    model = Diary
    success_url = reverse_lazy('diary:diary_list')


#todo
class TodoListView(ListView):
    template_name = 'todo/todo_list.html'
    model = Todo 
    context_object_name = 'todo_list'
    queryset = Todo.objects.all().order_by('-id')

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