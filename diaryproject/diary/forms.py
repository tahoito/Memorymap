from django import forms
from .models import Diary,Todo

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = {'date','title','text'}
        widget = {
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            }
        
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = {'id','memo',}
