from django import forms
from .models import Diary,Todo

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = {'date','title','text'}
        widgets = {
            'date': forms.TextInput(attrs={'class': 'form-control col-2'}),
            'title': forms.TextInput(attrs={'class': 'form-control col-2'}),
            'text': forms.Textarea(attrs={
                'class': 'form-control custom-textarea',
                'rows': 6  # ← 6行分の高さを確保
            }),  
        }

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = {'memo',}
        widgets = {
            'memo' : forms.TextInput(attrs={'class': 'form-control col-2'}),
        }
