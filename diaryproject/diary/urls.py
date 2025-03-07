from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    #diary
    path('', views.IndexView.as_view(), name='index'),
    path('diary/create/',views.DiaryCreateView.as_view(),name='diary_create'),
    path('diary/list/',views.DiaryListView.as_view(),name='diary_list'),
    path('diary/detail/<uuid:pk>/',views.DiaryDetailView.as_view(),name='diary_detail'),
    path('diary/update/<uuid:pk>/',views.DiaryUpdateView.as_view(),name='diary_update'),
    path('diary/delete/<uuid:pk>/',views.DiaryDeleteView.as_view(),name='diary_delete'),

    #todo
    path('todo/list',views.TodoListView.as_view(),name='todo_list'),
]